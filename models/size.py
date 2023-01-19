from sqlalchemy import ForeignKey
from models.models import db


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(80), nullable=False)
    product_name = db.Column(db.String, ForeignKey("product.name"))
    product = db.relationship("Product")

    # Product measurements to be stored in cm
    height = db.Column(db.Integer)
    hip_girth = db.Column(db.Integer)
    middle_hip = db.Column(db.Integer)  # Mapped onto hi hip from Chino template
    waist_girth = db.Column(db.Integer)
    waist_height = db.Column(db.Integer)
    inside_leg_length = db.Column(db.Integer)
    thigh_girth = db.Column(db.Integer)
    crotch_length = db.Column(db.Integer)
    knee_girth = db.Column(db.Integer)

    def __int__(
        self,
        size,
        product_name,
        height=None,
        hip_girth=None,
        middle_hip=None,
        waist_girth=None,
        waist_height=None,
        inside_leg_length=None,
        thigh_girth=None,
        crotch_length=None,
        knee_girth=None,
    ):

        self.size = size
        self.product_name = product_name
        self.height = height
        self.hip_girth = hip_girth
        self.middle_hip = middle_hip
        self.waist_girth = waist_girth
        self.waist_height = waist_height
        self.inside_leg_length = inside_leg_length
        self.thigh_girth = thigh_girth
        self.crotch_length = crotch_length
        self.knee_girth = knee_girth

    @staticmethod
    def convert_to_cm(size_units, measurement_val):
        if size_units == "imperial":
            return float(measurement_val) * 2.54
        else:
            return measurement_val
