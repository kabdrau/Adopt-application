"""Model for pet adopt."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "http://posfacturar.com/pos_organicnails/public/upload/default_image/default_pet.jpg"

class Pet(db.Model):
    """Pet class"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default = DEFAULT_IMAGE_URL)
    age = db.Column(db.Float(precision=2))
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)