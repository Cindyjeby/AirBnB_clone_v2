#!.usr/bin/python3
""" starts flask webapplication"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """routing to root"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """routing to /hbnb"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """routing c"""
    return "C {}".format(text)

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """routing to python"""
    text = text.replace('_', ' ')
    return "python {}".format(text)

@app.route('/number/<int>:n>', strict_slashes=False)
def is_a_numbet(n):
    """routing to n for ints"""
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)