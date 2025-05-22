# Solution to challenge 1

## user_prompt.py

```python
# Start with an empty file and use Copilot to generate the class
import re

class User:
    """
    A class to represent a user with attributes and validation.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        age (int): The age of the user.
    """

    def __init__(self, username: str, email: str, age: int):
        """
        Initialize a User instance with validation.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
            age (int): The age of the user.

        Raises:
            ValueError: If the email is invalid or age is not a positive integer.
        """
        print("Initializing User instance.")
        self.username = username
        self.email = self._validate_email(email)
        self.age = self._validate_age(age)
        print("User instance created successfully.")

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Validate the email address.

        Args:
            email (str): The email address to validate.

        Returns:
            str: The validated email address.

        Raises:
            ValueError: If the email is invalid.
        """
        print("Validating email address.")
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            print("Invalid email address provided.")
            raise ValueError("Invalid email address.")
        print("Email address validated successfully.")
        return email

    @staticmethod
    def _validate_age(age: int) -> int:
        """
        Validate the age.

        Args:
            age (int): The age to validate.

        Returns:
            int: The validated age.

        Raises:
            ValueError: If the age is not a positive integer.
        """
        print("Validating age.")
        if not isinstance(age, int) or age <= 0:
            print("Invalid age provided. Age must be a positive integer.")
            raise ValueError("Age must be a positive integer.")
        print("Age validated successfully.")
        return age


# Functionality to use the User class
if __name__ == "__main__":
    try:
        print("Starting the script to create a User instance.")
        username = input("Enter your username: ").strip()
        email = input("Enter your email: ").strip()
        age = int(input("Enter your age: ").strip())

        # Create a User instance
        user = User(username=username, email=email, age=age)
        print(f"User created successfully: {user.username}, {user.email}, {user.age}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
