from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/book_appt')
def book_appt():
    return render_template("book_appt.html")    
