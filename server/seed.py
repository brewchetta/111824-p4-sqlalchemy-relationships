from app import app
from models import db, Deli
from faker import Faker
from random import choice as random_choice

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Deli.query.delete()

        d1 = Deli(name="Mr Mango", location="Fort Greene", has_ice_cream=True, bacon_egg_cheese=True)
        d2 = Deli(name="Mr Kiwi", location="Bed Stuy", has_ice_cream=True, bacon_egg_cheese=True)
        d3 = Deli(name="Mr Pineapple", location="Park Slope", has_ice_cream=True, bacon_egg_cheese=True)

        db.session.add_all( [d1,d2,d3] )
        db.session.commit()

        for _ in range(150):
            faker_deli = Deli(
                name=faker.name(), 
                location=faker.address(),
                has_ice_cream=random_choice( [True, False] ),
                bacon_egg_cheese=random_choice( [True, False] )
            )

            db.session.add( faker_deli )
            print(f"Creating {faker_deli.name} deli....")

        db.session.commit()

        print("Seeding complete!")
