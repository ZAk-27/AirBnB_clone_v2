#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """shows Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """shows HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """shows “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """shows “Python ”, followed by the value of the variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """shows “n is a number” only if n is an int"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
