from . import db
from sqlalchemy.sql import func

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    appt_date = db.Column(db.String(20))
    appt_time = db.Column(db.String(20))
    set_date = db.Column(db.DateTime(timezone=True), default=func.now())
