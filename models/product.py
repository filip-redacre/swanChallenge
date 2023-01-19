from models.models import db


class Product(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    style_no = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    division = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String(50), nullable=False)

    def __init__(
        self, name, style_no, description, division, category, season, year, price
    ):
        self.name = name
        self.style_no = style_no
        self.description = description
        self.division = division
        self.category = category
        self.season = season
        self.year = year
        self.price = price
