# Solution to the challenge 3

## Promts for MCP connection with GitHub

<details>

<summary>Click for Solution</summary>

    List all issues from the repository "Technical-Bootcamp/L-Bank-Garage-Session".

</details>

<details>

<summary>Click for Solution</summary>

    Create a new issue titled "Adding a new functionality to the Flask app" and body:

    - use utils.py script in routes.py to call data
    - add app registration in routes.py script
    - use routes.py script in app.py application

    Assign this issue to Kasper1985
    - Add labels: "bug", "enhancement"

</details>

<details>

<summary>Click for Solution</summary>

    Change status of the issue with a title "Adding a new functionality to the Flask app" to "in progress"

</details>

<details>

<summary>Click for Solution</summary>

    Close the issue titled "Adding a new functionality to the Flask app" with the following comment:

    - The issue has been resolved by implementing the changes in the codebase.

</details>

## Results

<details>
<summary>Possible resulting files</summary>

## app.py

```python
import routes
from flask import Flask

app = Flask(__name__)

routes.register(app)

if __name__ == "__main__":
    app.run(debug=True)
```

## routes.py

```python
import utils

def register(app):
    """
    Register routes with the Flask app.
    
    :param app: Flask application instance
    """
    app.add_url_rule("/", "home", home)
    app.add_url_rule("/api/data", "get_data", get_data)

def home():
    return "Welcome to the Flask app!"

def get_data():
    return utils.get_data()
```

## utils.py

```python
def helper_function():
    return "This is a helper function."

def get_data():
    """
    Simulate fetching data from a database or an API.
    
    :return: Sample data
    """
    return {"name": "John Doe", "age": 30, "city": "New York"}
```

</details>
