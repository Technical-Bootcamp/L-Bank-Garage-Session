# Solution to challenge 1

## Run prompt with GitHub Copilot Edit Mode

<details>
<summary>Click for Solution #1</summary>

    Generate a `User` class with attributes

    - user name
    - email
    - age

</details>

<details>
<summary>Click for Solution #2</summary>

    Ensure that the provided Email is a valid email address

</details>

<details>
<summary>Click for Solution #3</summary>

    Ensure that the provided age is a number and positive

</details>

<details>
<summary>Click for Solution #4</summary>

    Extract the age validation in the same way as the email validation

</details>

<details>
<summary>Click for Solution #5</summary>

    Add logging of creation and validation steps

</details>

<details>
<summary>Click for Solution #6</summary>

    Add docstrings for class and method

</details>

## user_prompt.py

<details>
<summary>Possible resulting file</summary>

```python
# Start with an empty file and use Copilot to generate the class
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class User:
    """
    A class to represent a user with attributes for user name, email, and age.
    Includes validation for email and age during initialization.
    """

    def __init__(self, user_name: str, email: str, age: int):
        """
        Initialize a new User instance.

        Args:
            user_name (str): The name of the user.
            email (str): The email address of the user.
            age (int): The age of the user.

        Raises:
            ValueError: If the email is invalid or the age is not a positive integer.
        """
        logging.info("Creating a new User instance.")
        self.user_name = user_name
        logging.info(f"Validating email: {email}")
        if not self._is_valid_email(email):
            logging.error(f"Invalid email address: {email}")
            raise ValueError(f"Invalid email address: {email}")
        self.email = email
        logging.info(f"Validating age: {age}")
        if not self._is_valid_age(age):
            logging.error(f"Invalid age: {age}")
            raise ValueError(f"Age must be a positive integer: {age}")
        self.age = age
        logging.info("User instance created successfully.")

    def _is_valid_email(self, email: str) -> bool:
        """
        Validate the email address using a regex.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

    def _is_valid_age(self, age: int) -> bool:
        """
        Validate that the age is a positive integer.

        Args:
            age (int): The age to validate.

        Returns:
            bool: True if the age is a positive integer, False otherwise.
        """
        return isinstance(age, int) and age > 0


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

</details>
