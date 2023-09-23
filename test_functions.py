import unittest
from functions import DataManager, RecipeManager, UserManager, Authenticator, Message

class TestDataManager(unittest.TestCase):
    def setUp(self):
        # Set up test data 
        self.data_manager = DataManager('test_data_directory')

    def tearDown(self):
        # Clean up after the test
        pass

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
        test_recipes = [{'name': 'Recipe 1', 'ingredients': ['Ingredient 1', 'Ingredient 2']},
                        {'name': 'Recipe 2', 'ingredients': ['Ingredient 3', 'Ingredient 4']}]

        # Save test recipes
        self.recipe_manager.save_recipes(test_recipes)

        # Load the recipes and compare with the original
        loaded_recipes = self.recipe_manager.load_recipes()
        self.assertEqual(loaded_recipes, test_recipes)

    def test_save_recipes(self):
        # Test saving recipes
        test_recipes = [{'name': 'Recipe 1', 'ingredients': ['Ingredient 1', 'Ingredient 2']},
                        {'name': 'Recipe 2', 'ingredients': ['Ingredient 3', 'Ingredient 4']}]

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
            'user1@example.com': {'name': 'User 1', 'password': 'password1'},
            'user2@example.com': {'name': 'User 2', 'password': 'password2'}
        }

        # Save test user data
        self.user_manager.save_users(test_users)

        # Load the user data and compare with the original
        loaded_users = self.user_manager.load_users()
        self.assertEqual(loaded_users, test_users)

    def test_save_users(self):
        # Test saving user data
        test_users = {
            'user1@example.com': {'name': 'User 1', 'password': 'password1'},
            'user2@example.com': {'name': 'User 2', 'password': 'password2'}
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

if __name__ == '__main__':
    unittest.main()
