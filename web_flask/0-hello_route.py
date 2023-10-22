#!/usr/bin/python3
"""start flask webapplication"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    routing to root,
    strict_slashes ensures the url works when it ends both with or without /
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
