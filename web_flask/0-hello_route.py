#!/usr/bin/python3
""" Module that creates very basic Flask app.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_route():
    """ The 'root' route.
        Sends the "Hello HBNB!" text.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
