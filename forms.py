"""Forms for pet adopt."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional, DataRequired

choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=choices)
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=2)])
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=2)])
    available = BooleanField("Available?")