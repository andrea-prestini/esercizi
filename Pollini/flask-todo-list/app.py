from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index():
    welcome_message = 'Welcome to BICHER'
    return render_template('index.html', message=welcome_message)
