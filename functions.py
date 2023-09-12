import json
import os

# Define the paths to data files
recipes_file_path = os.path.join(os.path.dirname(__file__), 'data', 'recipes.json')
contact_file_path = os.path.join(os.path.dirname(__file__), 'data', 'contact.json')
users_file_path = os.path.join(os.path.dirname(__file__), 'data', 'users.json')

# Function to load data from a JSON file
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Function to save data to a JSON file
def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Function to load recipes from recipes.json
def load_recipes():
    return load_data(recipes_file_path)

# Function to save recipes to recipes.json
def save_recipes(recipes):
    save_data(recipes, recipes_file_path)

# Function to load contact messages from contact.json
def load_contact_messages():
    return load_data(contact_file_path)

# Function to save contact messages to contact.json
def save_contact_messages(messages):
    save_data(messages, contact_file_path)

# Function to load registered users from users.json
def load_users():
    return load_data(users_file_path)

# Function to save registered users to users.json
def save_users(users):
    # Create a deep copy of users to avoid modifying the original data
    users_copy = {email: user_info.copy() for email, user_info in users.items()}

    # Ensure that passwords are stored as strings
    for user_info in users_copy.values():
        user_info['password'] = user_info['password'].decode('utf-8') if isinstance(user_info['password'], bytes) else user_info['password']

    with open(users_file_path, 'w', encoding='utf-8') as file:
        json.dump(users_copy, file, indent=4, ensure_ascii=False)


# Check if a user is authenticated
def is_authenticated(session):
    return 'user_id' in session
