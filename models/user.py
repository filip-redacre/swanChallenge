from models.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # User measurements to be stored in cm
    height = db.Column(db.Integer)
    hip_girth = db.Column(db.Integer)
    middle_hip = db.Column(db.Integer)  # Mapped onto hi hip from Chino template
    waist_girth = db.Column(db.Integer)
    waist_height = db.Column(db.Integer)
    inside_leg_length = db.Column(db.Integer)
    thigh_girth = db.Column(db.Integer)
    crotch_length = db.Column(db.Integer)
    knee_girth = db.Column(db.Integer)
