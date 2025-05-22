# Solution to the challenge 3

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
