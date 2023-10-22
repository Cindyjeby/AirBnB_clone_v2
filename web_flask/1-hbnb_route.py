#!/usr/bin/python3
"""start a flask webapplication"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strick_slashes=False)
def hello_hbnb():
    """
    route to root, strict_slashes to ensure the
    url works when it ends both or either /
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    routing to hbnb
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
