import json

from flask import Blueprint, request

from models.models import db
from models.product import Product
from models.size import Size

api = Blueprint("api", __name__, template_folder="templates")


@api.route("/")
def hello_world():
    return "Hello World!"


# Upload tech pack to be parsed
@api.route("/tech_pack", methods=["POST"])
def parse_tech_pack():
    tech_pack = json.loads(request.get_data())
    new_product = Product(
        name=tech_pack["name"],
        style_no=tech_pack["style_no"],
        description=tech_pack["description"],
        division=tech_pack["division"],
        category=tech_pack["category"],
        season=tech_pack["season"],
        year=tech_pack["year"],
        price=tech_pack["price"],
    )
    db.session.add(new_product)

    for size, val in tech_pack["sizes"].items():
        new_size = Size(
            size=size,
            size_units=tech_pack["size_units"],
            product_name=tech_pack["name"],
            middle_hip=val["middle_hip"],
            waist_girth=val["waist_girth"],
            waist_height=val["waist_height"],
            inside_leg_length=val["inside_leg_length"],
            thigh_girth=val["thigh_girth"],
            knee_girth=val["knee_girth"],
            crotch_length=val["crotch_length"],
        )
        db.session.add(new_size)

    db.session.commit()
    return "Tech Pack successfully added"


@api.route("/product/all", methods=["GET"])
def get_all_products():
    all_products = Product.query.all()

    return all_products


@api.route("/product", methods=["GET"])
def get_product():
    kwargs = {
        "name": request.args.get("name"),
        "division": request.args.get("division"),
        "category": request.args.get("category"),
        "season": request.args.get("season"),
        "year": request.args.get("year"),
        "price": request.args.get("price"),
    }

    Product.query.filter_by(**kwargs)

    return "Hello World!"


@api.route("/product/<name>", methods=["PUT"])
def update_product(name):
    return "Hello World!"


@api.route("/product/<name>", methods=["DELETE"])
def delete_product(name):
    return "Hello World!"
