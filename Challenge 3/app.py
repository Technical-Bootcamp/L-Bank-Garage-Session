from flask import Flask
app = Flask(__name__)

# Import routes and utils
import routes
import utils

if __name__ == "__main__":
    app.run(debug=True)
