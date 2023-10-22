#!/usr/bin/python3
"""module for C is fun"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """starts a Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """C is fun"""
    text = text.replace('_', ' ' )
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)