# Solution to the challenge 3

## Prompts for MCP connection with GitHub

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

## Prompts for Code generation in Ask Mode

<details>

<summary>Click for Solution (utils.py)</summary>

    Generate a new function `get_data` returning and simple data as JSON.

</details>

<details>

<summary>Click for Solution (routes.py)</summary>

    Add a route `/api/data` which gets data from the utils script.

</details>

<details>

<summary>Click for Solution (routes.py)</summary>

    Add a function to register all routes for the provided app from flask.

</details>

<details>

<summary>Click for Solution (app.py)</summary>

    Add registration of routes from #file:routes.py for initialized flask app.

</details>

## Results

<details>
<summary>Possible resulting files</summary>

### app.py

```python
from flask import Flask
app = Flask(__name__)

from routes import register_routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
```

### routes.py

```python
from utils import get_data

def register_routes(app):
    @app.route("/")
    def home():
        return "Welcome to the Flask app!"

    @app.route("/api/data")
    def api_data():
        return get_data(), 200, {"Content-Type": "application/json"}
```

### utils.py

```python
import json

def get_data():
    data = {
        "name": "L-Bank",
        "challenge": 3,
        "status": "active"
    }
    return json.dumps(data)

def helper_function():
    return "This is a helper function."
```

</details>
