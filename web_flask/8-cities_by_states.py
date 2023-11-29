#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_clss():
    """shows the states and cities listed in alpheu order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_mn(exception):
    """closing the storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
