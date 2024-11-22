#!/usr/bin/env python3
"""
Flask app with Babel, Basic Babel setup, Get locale from request
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
"""Use that class as config for the app"""


@app.route('/')
def root():
    """ basic Flask app """
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
