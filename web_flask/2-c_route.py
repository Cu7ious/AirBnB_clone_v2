#!/usr/bin/python3
""" Module that creates very basic Flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_route():
    """ The 'root' route.
        Sends the "Hello HBNB!" text
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ The 'hbnb' route.
        Sends the "HBNB" text
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ The 'c' route with the text varible subroute.
        Sends the "C" with the complimented text

        @text: the variable subroute
    """
    return "C" + " " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
