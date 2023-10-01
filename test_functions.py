import unittest
import os
from functions import DataManager, RecipeManager, UserManager, Authenticator, ContactManager, Message

class TestDataManager(unittest.TestCase):
  def setUp(self):
    # Set up test data directory and create it if it doesn't exist
    self.test_data_directory = 'test_data_directory'
    if not os.path.exists(self.test_data_directory):
      os.makedirs(self.test_data_directory)
    
    # Initialize DataManager with the test data directory
    self.data_manager = DataManager(self.test_data_directory)

  def tearDown(self):
    # Clean up: Remove any test data files created during the test
    test_data_file = os.path.join(self.test_data_directory, 'test_data.json')
    if os.path.exists(test_data_file):
      os.remove(test_data_file)

  def test_load_data(self):
    # Test loading data 
    file_name = 'test_data.json'
    test_data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]

    # Save test data 
    self.data_manager.save_data(test_data, file_name)

    # Load the data and compare with the original
    loaded_data = self.data_manager.load_data(file_name)
    self.assertEqual(loaded_data, test_data)

  def test_save_data(self):
    # Test saving data 
    file_name = 'test_data.json'
    test_data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]

    # Save the test data 
    self.data_manager.save_data(test_data, file_name)

    # Load the data and compare with the original
    loaded_data = self.data_manager.load_data(file_name)
    self.assertEqual(loaded_data, test_data)

class TestRecipeManager(unittest.TestCase):
  def setUp(self):
    # Set up test data
    self.recipe_manager = RecipeManager('test_data_directory')

  def tearDown(self):
    # Clean up after the test
    pass

  def test_load_recipes(self):
    # Test loading recipes
    test_recipes = [
      {
        "user_id": "test@test.com",
        "id": 1,
        "name": "test",
        "category": "Main",
        "difficulty": "Easy",
        "ingredients": [
          "test",
          "test",
          "test"
        ],
        "instructions": [
          "test",
          "test"
        ],
        "image_filename": "test.webp"
      },
      {
        "user_id": "test2@test.com",
        "id": 2,
        "name": "test2",
        "category": "Main",
        "difficulty": "Easy",
        "ingredients": [
          "test2",
          "test2",
          "test2"
        ],
        "instructions": [
          "test2",
          "test2"
        ],
        "image_filename": "test2.webp"
      }
    ]

    # Save test recipes
    self.recipe_manager.save_recipes(test_recipes)

    # Load the recipes and compare with the original
    loaded_recipes = self.recipe_manager.load_recipes()
    self.assertEqual(loaded_recipes, test_recipes)

  def test_save_recipes(self):
    # Test saving recipes
    test_recipes = [
    {
      "user_id": "test@test.com",
      "id": 1,
      "name": "test",
      "category": "Main",
      "difficulty": "Easy",
      "ingredients": [
        "test",
        "test",
        "test"
      ],
      "instructions": [
        "test",
        "test"
      ],
      "image_filename": "test.webp"
    },
    {
      "user_id": "test2@test.com",
      "id": 2,
      "name": "test2",
      "category": "Main",
      "difficulty": "Easy",
      "ingredients": [
        "test2",
        "test2",
        "test2"
      ],
      "instructions": [
        "test2",
        "test2"
      ],
      "image_filename": "test2.webp"
    }
  ]

    # Save the test recipes
    self.recipe_manager.save_recipes(test_recipes)

    # Load the recipes and compare with the original
    loaded_recipes = self.recipe_manager.load_recipes()
    self.assertEqual(loaded_recipes, test_recipes)


class TestUserManager(unittest.TestCase):
  def setUp(self):
    # Set up test data
    self.user_manager = UserManager('test_data_directory')

  def tearDown(self):
    # Clean up after the test
    pass

  def test_load_users(self):
    # Test loading user data
    test_users = {
      'test@test.com': {
        'user_id': 1,
        'name': 'test',
        'email': 'test@test.com',
        'password': 'testpasword',
        'profile_image': 'test.webp'
      },
      'test2@test.com': {
        'user_id': 2,
        'name': 'test2',
        'email': 'test2@test.com',
        'password': 'testpasword2',
        'profile_image': 'test2.webp'
      }
    }

    # Save test user data
    self.user_manager.save_users(test_users)

    # Load the user data and compare with the original
    loaded_users = self.user_manager.load_users()
    self.assertEqual(loaded_users, test_users)

  def test_save_users(self):
      # Test saving user data
      test_users = {
        'test@test.com': {
          'user_id': 1,
          'name': 'test',
          'email': 'test@test.com',
          'password': 'testpasword',
          'profile_image': 'test.webp'
        },
        'test2@test.com': {
          'user_id': 2,
          'name': 'test2',
          'email': 'test2@test.com',
          'password': 'testpasword2',
          'profile_image': 'test2.webp'
        }
      }

      # Save the test user data
      self.user_manager.save_users(test_users)

      # Load the user data and compare with the original
      loaded_users = self.user_manager.load_users()
      self.assertEqual(loaded_users, test_users)


class TestAuthenticator(unittest.TestCase):
  def setUp(self):
    # Set up test data
    pass

  def tearDown(self):
    # Clean up after the test
    pass

  def test_is_authenticated(self):
    # Test the is_authenticated method of the Authenticator
    authenticated_session = {'user_id': 1, 'username': 'user1'}
    unauthenticated_session = {'username': 'user2'}

    # Check if authenticated session returns True
    self.assertTrue(Authenticator.is_authenticated(authenticated_session))

    # Check if unauthenticated session returns False
    self.assertFalse(Authenticator.is_authenticated(unauthenticated_session))

class TestMessage(unittest.TestCase):
  def setUp(self):
    # Set up test data
    pass

  def tearDown(self):
    # Clean up after the test
    pass

  def test_to_dict(self):
    # Test converting a Message object to a dictionary
    test_message = Message('Sender 1', 'sender1@example.com', 'Message 1')

    expected_dict = {'name': 'Sender 1', 'email': 'sender1@example.com', 'comment': 'Message 1'}
    self.assertEqual(test_message.to_dict(), expected_dict)

class TestContactManager(unittest.TestCase):
  def setUp(self):
    # Set up test data directory and create it if it doesn't exist
    self.test_data_directory = 'test_data_directory'
    if not os.path.exists(self.test_data_directory):
      os.makedirs(self.test_data_directory)
    
    # Initialize ContactManager with the test data directory
    self.contact_manager = ContactManager(self.test_data_directory)

  def tearDown(self):
    # Clean up after the test
    pass

  def test_save_contact_messages(self):
    # Test saving contact messages
    test_messages = [
      Message('Sender 1', 'sender1@example.com', 'Message 1'),
      Message('Sender 2', 'sender2@example.com', 'Message 2')
    ]

    # Save the test contact messages
    self.contact_manager.save_contact_messages(test_messages)

    # Load the contact messages as dictionaries
    loaded_messages = self.contact_manager.load_contact_messages()

    # Convert the loaded dictionaries to Message objects
    loaded_message_objects = [Message(msg['name'], msg['email'], msg['comment']) for msg in loaded_messages]

    # Compare the loaded Message objects with the original messages
    self.assertEqual(len(loaded_message_objects), len(test_messages))
    for i in range(len(test_messages)):
      self.assertEqual(loaded_message_objects[i].to_dict(), test_messages[i].to_dict())


if __name__ == '__main__':
  unittest.main()
