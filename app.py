from flask import Flask
from werkzeug.utils import import_string

from api import api
from models.models import db

cfg = import_string("config_module.DevelopmentConfig")()
app = Flask(__name__)
app.config.from_object(cfg)
app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URI"]

# DB init
db.init_app(app)
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(api)


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], test=app.config["TEST"])
