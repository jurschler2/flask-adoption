"""Flask app for adopt app."""

from flask import Flask, render_template, request, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from form import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/")
def display_homepage():
    """ Display the pet list """

    pets = Pet.query.all()
    return render_template("pets_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def display_add_pet_form():
    """ Display and validate add pet form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data or None
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, age=age, photo_url=photo_url,
                  notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet_form.html", form=form)
