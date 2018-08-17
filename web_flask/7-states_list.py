#!/usr/bin/python3
""" This module starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ The "states_list" route.
        Sends a corresponding template.
    """
    states = storage.all(State).values()
    # print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ Hook that runs before app would be closed
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
