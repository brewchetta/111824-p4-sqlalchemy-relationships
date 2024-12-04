from app import app
from models import db, Deli, Hamburger

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Deli.query.delete()
        Hamburger.query.delete()

        d1 = Deli(name="Mr Mango", has_bodega_cat=True)
        d2 = Deli(name="Mr Kiwi", has_bodega_cat=True)
        d3 = Deli(name="Mr Pineapple", has_bodega_cat=True)

        db.session.add_all( [d1,d2,d3] )
        db.session.commit()

        h1 = Hamburger(name="Rodeo Burger", deli_id=d1.id)
        h2 = Hamburger(name="Hulk Smash Burger", deli_id=d1.id)
        h3 = Hamburger(name="Veggie Burger", deli_id=d2.id)
        h4 = Hamburger(name="Derrick Zoolander's Burger for Children Who Don't Eat Very Good", deli_id=d3.id)

        db.session.add_all( [h1,h2,h3,h4] )
        db.session.commit()

        print("Seeding complete!")
