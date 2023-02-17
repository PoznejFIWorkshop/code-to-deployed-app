# This file contains webserver around our logic.
# You can ignore it. 

from random import randint  # Standard library

from flask import Flask, url_for  # Library downloaded using pip
from markupsafe import escape  # Library downloaded using pip

from logic import factorial  # Our own file logic.py
from utils import open_browser_with_delay, modify_int_max_str_digits  # Our own file utils.py

app = Flask(__name__)

@app.route('/')
def homepage():
    n = randint(0, 42)
    n_url = url_for('factorial_get', n=n)
    return f'Hello there ... try going to <a href="{n_url}">{n_url}</a>'


@app.route('/<int:n>')
def factorial_get(n: int):
    return f'Factorial of {escape(n)} is {factorial(n)}. <a href="/">Go back</a>'
# Function escape makes sure the website is not vulnerable to Cross-Site Scripting (XSS).


modify_int_max_str_digits()

if __name__ == '__main__':
    open_browser_with_delay(url="http://127.0.0.1", delay=2)
    app.run(port=80)
