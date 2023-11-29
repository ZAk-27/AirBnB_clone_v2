#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
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
    """shows “C ” followed by the value of the varb"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """shows “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """shows “n is a number” only if n is an int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """show a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersoddoreven(n):
    """show a HTML page only if n is an integer"""
    if n % 2 == 0:
        oddoreven = 'even'
    else:
        oddoreven = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
