"""Pet adopt application."""

from crypt import methods
from flask import Flask, request, redirect, render_template, flash
from model import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from seed import create_pets
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.drop_all()
db.create_all()

create_pets()

#### Part1 ####

@app.route("/")
def list_pets():
    """Show all pets."""

    pets = Pet.query.order_by(Pet.available.desc(), Pet.name).all()
    return render_template("show_pets.html", pets=pets)

@app.route("/add", methods=["GET","POST"])
def add_pet():
    """"Add new pet from."""

    form = AddPetForm()

    if form.validate_on_submit():
        # POST route
        # raise
        data = {key: val for key, val in form.data.items() if key != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} was added.", "success")
        return redirect("/")
    else:
        # GET route
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet form."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        # POST route
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} was updated.", "success")
        return redirect('/')
    else:
        # GET route
        return render_template("edit_pet_form.html", pet=pet, form=form)

@app.route("/<int:pet_id>/delete", methods=["GET", "POST"])
def delete_pet(pet_id):
    """Delete pet."""

    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    flash(f"{pet.name} was deleted.", "danger")

    return redirect("/")