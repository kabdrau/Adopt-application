"""Seed file to make sample data for pets db."""

from model import Pet, db

def create_pets():
    
    # Add pets
    whiskey = Pet(name='Whiskey', 
        species="dog", 
        photo_url="http://cdn.akc.org/content/article-body-image/lab_puppy_dog_pictures.jpg",
        age=1.666)
    rex = Pet(name='Rex',
        species="dog",
        age=2.5,
        notes="adopted",
        available=False
        )
    pam = Pet(name='Pamela', 
        species="cat",
        photo_url="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_3x2.jpg")

    lolly = Pet(name='Lolly', 
        species="cat",
        photo_url="https://i.pinimg.com/originals/01/6f/72/016f72c5812e1b8f71bdbf19d8c7558b.jpg",
        age=0.25,
        notes="adopted",
        available=False)

    steven = Pet(name="Steven", 
        species="dog", 
        photo_url="https://kb.rspca.org.au/wp-content/uploads/2018/11/golder-retriever-puppy.jpeg")

    harry = Pet(name="Harry", 
        species="dog",
        photo_url="https://cdn.cnn.com/cnnnext/dam/assets/201030094143-stock-rhodesian-ridgeback-super-tease.jpg",
        age=2.333,
        notes="adopted",
        available=False)

    # Add new objects to session, so they'll persist
    db.session.rollback()
    db.session.add(whiskey)
    db.session.add(rex)
    db.session.add(pam)
    db.session.add(lolly)
    db.session.add(steven)
    db.session.add(harry)

    # Commit--otherwise, this never gets saved!
    db.session.commit()