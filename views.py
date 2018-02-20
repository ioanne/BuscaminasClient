from flask import Flask, render_template, request, redirect, url_for
from forms import BuscaminasForm
import requests

app = Flask(__name__)
app.secret_key = 'kjhKJHJKhjkHJKhjkhKJhkjHJKhkjHKJhkJHkj89798h87H98kLoH6820D0s9s'


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'home'

if __name__ == '__main__':
    app.run(debug=False, port=5000)