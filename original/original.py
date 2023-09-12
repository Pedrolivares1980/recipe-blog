from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, make_response
import json
import os
import bcrypt

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Paths to data files
recipes_file_path = os.path.join(app.root_path, 'data', 'recipes.json')
contact_file_path = os.path.join(app.root_path, 'data', 'contact.json')
users_file_path = os.path.join(app.root_path, 'data', 'users.json')

# Function to load recipes from recipes.json
def load_recipes():
    with open(recipes_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to save recipes to recipes.json
def save_recipes(recipes):
    with open(recipes_file_path, 'w', encoding='utf-8') as file:
        json.dump(recipes, file, indent=4, ensure_ascii=False)

# Function to load contact messages from contact.json
def load_contact_messages():
    if os.path.exists(contact_file_path):
        with open(contact_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Function to save contact messages to contact.json
def save_contact_messages(messages):
    with open(contact_file_path, 'w', encoding='utf-8') as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)

# Function to load registered users from users.json
def load_users():
    if os.path.exists(users_file_path):
        with open(users_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

# Function to save registered users to users.json
def save_users(users):
    # Convert the hashed passwords to strings before saving
    users_copy = users.copy()  # Create a copy of users to avoid modifying the original data
    for email, user_info in users_copy.items():
        user_info['password'] = user_info['password'].decode('utf-8')

    with open(users_file_path, 'w', encoding='utf-8') as file:
        json.dump(users_copy, file, indent=4, ensure_ascii=False)

# Check if a user is authenticated
def is_authenticated():
    return 'user_id' in session

# Add 'is_authenticated' to the global Jinja2 context
app.jinja_env.globals.update(is_authenticated=is_authenticated)

# Route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Load registered users
        registered_users = load_users()

        # Check if the email is already registered
        if email in registered_users:
            flash('Email is already registered. Please log in.')
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
        save_users(registered_users)

        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register')

# Route for the home page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')

# Route for the recipes page
@app.route('/recipes')
def recipes():
    recipes = load_recipes()
    return render_template('recipes.html', title='Recipes', recipes=recipes)

# Route to add a new recipe in the profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')  # Get 'user_id' from the session if it exists
    if user_id:
        if request.method == 'POST':
            # Get data from the recipe form
            recipe_name = request.form['recipe_name']
            category = request.form['category']
            difficulty = request.form['difficulty']
            ingredients = request.form['ingredients'].split('\n')
            instructions = request.form['instructions'].split('\n')
            image_url = request.form['image_url']

            # Load current recipes
            recipes = load_recipes()

            # Create a new recipe object associated with the user's ID
            new_recipe = {
                'user_id': user_id,
                'id': len(recipes) + 1,  # Generate a unique recipe ID
                'name': recipe_name,
                'category': category,
                'difficulty': difficulty,
                'ingredients': ingredients,
                'instructions': instructions,
                'image_path': image_url
            }

            # Add the new recipe to the list of recipes
            recipes.append(new_recipe)

            # Save the updated recipes to recipes.json
            save_recipes(recipes)

            flash('Recipe added successfully.', 'success')
            return redirect(url_for('profile'))

        # Load recipes for the current user (filter by user ID)
        user_recipes = [recipe for recipe in load_recipes() if recipe.get('user_id') == user_id]
        return render_template('profile.html', title='Profile', recipes=user_recipes)

    flash('You must log in to access your profile.', 'error')
    return redirect(url_for('login'))

# Route to delete a recipe
@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    user_id = session.get('user_id')  # Get 'user_id' from the session if it exists
    if user_id:
        # Load recipes from your data source (e.g., recipes.json)
        recipes = load_recipes()

        # Find the recipe with the given recipe_id and user_id
        for recipe in recipes:
            if recipe.get('id') == recipe_id and recipe.get('user_id') == user_id:
                recipes.remove(recipe)
                # Save the updated recipes back to your data source
                save_recipes(recipes)
                return '', 204  # No content, indicating successful deletion

        # If the recipe doesn't exist or doesn't belong to the user, return an error response
        return json.dumps({'error': 'Recipe not found or unauthorized'}), 404

    # If the user is not logged in, return an error response
    return json.dumps({'error': 'Unauthorized'}), 401


# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']

        contact_messages = load_contact_messages()

        new_message = {
            'name': name,
            'email': email,
            'comment': comment
        }

        contact_messages.append(new_message)

        save_contact_messages(contact_messages)

        flash('Message sent successfully. We will get back to you soon.', 'success')
        return redirect(url_for('index'))

    return render_template('contact.html', title='Contact Us')


# Route to log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = load_users()

        if email in users:
            if bcrypt.checkpw(password.encode('utf-8'), users[email]['password'].encode('utf-8')):
                session['user_id'] = email
                flash('Login successful.', 'success')
                return redirect(url_for('profile'))
        
        flash('Incorrect credentials. Please try again.', 'error')

    return render_template('login.html', title='Login')

# Route to log out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have logged out.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

