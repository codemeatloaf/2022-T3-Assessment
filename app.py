# guide: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# imports
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def wndw1():
    return render_template('wndw1.html')