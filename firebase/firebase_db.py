import firebase_admin
from firebase_admin import credentials, db

# Import your service account key and database URL
from config import Config

# Initialize the app
cred_obj = credentials.Certificate(Config.SERVICE_ACCOUNT_KEY)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': Config.DATABASE_URL
})

# Reference to the root of the database
root_ref = db.reference()
users_ref = root_ref.child('Users')  # Reference to the 'users' node


def add_latest_disease(phone: str, latest_disease: str):
    """
        Add a new Latest disease diagnose to the Firebase database.

        Args:
            phone (str): The phone number of the user.
            latest_disease (str): The latest disease diagnose.

        Returns:
            None

        Raises:
            Exception: If an error occurs while adding the user.
        """
    try:
        users_ref.child(phone).child('latest_disease').set(latest_disease)
        print("Latest disease added successfully!")
    except Exception as e:
        print(f"Error adding Latest disease: {e}")


def add_user(phone: str, full_name: str, location_country: str, location_city: str):
    """
    Add a new user to the Firebase database.

    Args:
        phone (str): The phone number of the user.
        full_name (str): The full name of the user.
        location_country (str): The country where the user is located.
        location_city (str): The city where the user is located.

    Returns:
        None

    Raises:
        Exception: If an error occurs while adding the user.
    """
    try:
        users_ref.child(phone).set({
            'full_name': full_name,
            'location_country': location_country,
            'location_city': location_city
        })
        print("User added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")


def get_user(phone: str):
    """
    Retrieve user data from the Firebase database.

    Args:
        phone (str): The phone number of the user to retrieve.

    Returns:
        dict or None: A dictionary containing user data if the user exists, else None.

    Raises:
        Exception: If an error occurs while retrieving user data.
    """
    try:
        user_data = users_ref.child(phone).get()
        if user_data:
            return user_data
        else:
            print("User not found.")
            return None
    except Exception as e:
        print(f"Error getting user data: {e}")
        return None


def update_user(phone: str, update_data: dict):
    """
    Update user data in the Firebase database.

    Args:
        phone (str): The phone number of the user to update.
        update_data (dict): A dictionary containing the updated user data attributes.

    Returns:
        None

    Raises:
        Exception: If an error occurs while updating user data.
    """
    try:
        users_ref.child(phone).update(update_data)
        print("User data updated successfully!")
    except Exception as e:
        print(f"Error updating user data: {e}")


def delete_user(phone: str):
    """
    Delete a user from the Firebase database.

    Args:
        phone (str): The phone number of the user to delete.

    Returns:
        None

    Raises:
        Exception: If an error occurs while deleting the user.
    """
    try:
        users_ref.child(phone).delete()
        print("User deleted successfully!")
    except Exception as e:
        print(f"Error deleting user: {e}")
