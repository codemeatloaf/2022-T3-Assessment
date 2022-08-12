# imports
from flask import Flask, render_template
import datetime

app = Flask(__name__)

# index
@app.route('/')

def index():
    return render_template('wndw1.html',  utc_dt=datetime.datetime.utcnow())

# guide to html section
@app.route('/guide/')
def guide():
    return render_template('wndw0.html')    

# about section
@app.route('/about/')
def about():
    return render_template('wndw2.html')
