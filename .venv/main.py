# imports
from flask import render_template, Blueprint
import datetime

# main and database 
main = Blueprint('main', __name__)

# index
@main.route('/')

def index():
    return render_template('wndw1.html',  utc_dt=datetime.datetime.utcnow())

# guide to html section
@main.route('/guide')
def guide():
    return render_template('wndw0.html')    

# about section
@main.route('/about')
def about():
    return render_template('wndw2.html')

# profile section
@main.route('/profile')
def about():
    return render_template('wndw3.html')
