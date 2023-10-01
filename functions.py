import json
import os

class DataManager:
  def __init__(self, data_directory):
    """
    Initialize a DataManager object.

    """
    self.data_directory = data_directory

  def load_data(self, file_name):
    """
    Load data from a JSON file.

    """
    file_path = os.path.join(self.data_directory, file_name)
    if os.path.exists(file_path):
      with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    return []

  def save_data(self, data, file_name):
    """
    Save data to a JSON file.

    """
    file_path = os.path.join(self.data_directory, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=4, ensure_ascii=False)

class RecipeManager(DataManager):
  def __init__(self, data_directory):
    """
    Initialize a RecipeManager object.

    """
    super().__init__(data_directory)
    self.recipes_file = 'recipes.json'

  def load_recipes(self):
    """
    Load recipes from recipes.json.

    """
    return self.load_data(self.recipes_file)

  def save_recipes(self, recipes):
    """
    Save recipes to recipes.json.

    """
    self.save_data(recipes, self.recipes_file)

class ContactManager(DataManager):
  def __init__(self, data_directory):
    """
    Initialize a ContactManager object.

    """
    super().__init__(data_directory)
    self.contact_file = 'contact.json'

  def load_contact_messages(self):
    """
    Load contact messages from contact.json

    """
    return self.load_data(self.contact_file)

  def save_contact_messages(self, messages):
    """
    Save contact messages to contact.json

    """
    self.save_data([message.to_dict() for message in messages], self.contact_file)

class UserManager(DataManager):
  def __init__(self, data_directory):
    """
    Initialize a UserManager object.

    """
    super().__init__(data_directory)
    self.users_file = 'users.json'

  def load_users(self):
    """
    Load user data from users.json

    """
    return self.load_data(self.users_file)

  def save_users(self, users):
    """
    Save user data to users.json

    """
    # Create a deep copy of users to avoid modifying the original data
    users_copy = {email: user_info.copy() for email, user_info in users.items()}

    # Ensure that passwords are stored as strings
    for user_info in users_copy.values():
      user_info['password'] = user_info['password'].decode('utf-8') if isinstance(user_info['password'], bytes) else user_info['password']

    self.save_data(users_copy, self.users_file)

class Authenticator:
  @staticmethod
  def is_authenticated(session):
    """
    Check if a user is authenticated based on the session.

    """
    return 'user_id' in session

class Message:
  def __init__(self, name, email, comment):
    """
    Initialize a Message object.

    """
    self.name = name
    self.email = email
    self.comment = comment

  def to_dict(self):
    """
    Convert the message to a dictionary.

    """
    return {
      'name': self.name,
      'email': self.email,
      'comment': self.comment
    }

