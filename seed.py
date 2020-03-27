from models import Pet, db
from app import app


db.drop_all()
db.create_all()

Pet.query.delete

# Name, Species, Age, Photo URL, Available, Notes,

pet1 = Pet(name="Spot", species="Dog", age="young", available=True)
db.session.add(pet1)
db.session.commit()
