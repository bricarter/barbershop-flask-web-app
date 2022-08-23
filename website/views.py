from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Appointment

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/book_appt', methods = ['GET', 'POST'])
def book_appt():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        appt_date = request.form.get('appt_date')
        appt_time = request.form.get('appt_time')

        conflicting_appt = Appointment.query.filter_by(appt_date = appt_date).filter_by(appt_time = appt_time).first()

        if conflicting_appt:
            flash('This slot is not available please choose a different date or time.', category='error')
        else:
            new_appt = Appointment(first_name=first_name, last_name=last_name, appt_date=appt_date, appt_time=appt_time)
            db.session.add(new_appt)
            db.session.commit()

            flash('Appointment booked successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template("book_appt.html")    
