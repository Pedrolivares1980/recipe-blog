from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os
import bcrypt
from functions import RecipeManager, ContactManager, UserManager, Authenticator, Message

app = Flask(__name__, static_folder='static')
app.secret_key = 'c86522f1d36832cb56a3b29716986d607ac42dfc'

# Paths to data files
data_dir = os.path.join(os.path.dirname(__file__), 'data')
recipe_manager = RecipeManager(data_dir)
contact_manager = ContactManager(data_dir)
user_manager = UserManager(data_dir)
authenticator = Authenticator()

# Add 'is_authenticated' to the global Jinja2 context
app.jinja_env.globals.update(is_authenticated=authenticator.is_authenticated)

# Route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Load registered users
        registered_users = user_manager.load_users()

        # Check if the email is already registered
        if email in registered_users:
            flash(('Email is already registered. Please log in.', 'danger'))
            return redirect(url_for('login'))

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store user information in the dictionary
        user_id = len(registered_users) + 1  # Generate a unique user ID
        registered_users[email] = {
            'user_id': user_id,
            'name': name,
            'email': email,
            'password': hashed_password
        }

        # Save the registered users to users.json
        user_manager.save_users(registered_users)

        flash(('Registration successful. Please log in.', 'success'))
        return redirect(url_for('login'))

    return render_template('register.html', title='Register')


# Route for home page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')

# Route to log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Load registered users
        users = user_manager.load_users()

        user = users.get(email)

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['user_id'] = email
            flash(('Login successful.', 'success'))
            return redirect(url_for('profile'))

        flash(('Incorrect credentials. Please try again.', 'danger'))

    return render_template('login.html', title='Login')


@app.route('/recipes')
def recipes_page():
    # Load recipes from the data file
    recipes = recipe_manager.load_recipes()

    return render_template('recipes.html', title='Recipes', recipes=recipes)

# Route to profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')  # Get 'user_id' from the session if it exists

    if user_id:
        # Load recipes from the data file
        recipes = recipe_manager.load_recipes()

        if request.method == 'POST':
            # Get data from the recipe form
            recipe_name = request.form['recipe_name']
            category = request.form['category']
            difficulty = request.form['difficulty']
            ingredients = request.form['ingredients'].split('\n')
            instructions = request.form['instructions'].split('\n')
            image_url = request.form['image_url']

            # Create a new recipe object associated with the user's ID
            new_recipe = {
                'user_id': user_id,
                'id': len(recipes) + 1, 
                'recipe_name': recipe_name,
                'category': category,
                'difficulty': difficulty,
                'ingredients': ingredients,
                'instructions': instructions,
                'image_url': image_url
            }

            recipes.append(new_recipe)
            recipe_manager.save_recipes(recipes)

            flash(('Recipe added successfully. Thank you for sharing.', 'success'))
            
            # Redirect to the profile page after adding a recipe
            return redirect(url_for('profile'))

        # Load recipes for the current user (filter by user ID)
        user_recipes = [recipe for recipe in recipes if recipe.get('user_id') == user_id]
        return render_template('profile.html', title='Profile', recipes=user_recipes)

    flash(('You must log in to access your profile.', 'danger'))
    return redirect(url_for('login'))


# Route to delete a recipe by ID
@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    user_id = session.get('user_id')

    if user_id:
        # Load recipes from the data file
        recipes = recipe_manager.load_recipes()

        # Find the recipe with the given recipe_id and user_id
        recipe_to_delete = next((recipe for recipe in recipes if recipe.get('id') == recipe_id and recipe.get('user_id') == user_id), None)

        if recipe_to_delete:
            recipes.remove(recipe_to_delete)
            recipe_manager.save_recipes(recipes)

            # Respond with a JSON success message
            return jsonify({'status': 'success', 'message': 'Recipe deleted successfully'}), 200

        # If the recipe doesn't exist or doesn't belong to the user, return an error response
        return jsonify({'status': 'error', 'message': 'Recipe not found or unauthorized'}), 404

    # If the user is not logged in, return an unauthorized response
    return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401


# Route to log out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash(('You have logged out. Please come back soon.', 'success'))
    return redirect(url_for('index'))

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']

        new_message = Message(name, email, comment)

        # Use the contact_manager to save the new message
        contact_manager.save_contact_messages([new_message])

        flash(('Message sent successfully. We will get back to you soon. Thank you.', 'success'))
        return redirect(url_for('index'))

    return render_template('contact.html', title='Contact Us')

if __name__ == '__main__':
    app.run(debug=True)
