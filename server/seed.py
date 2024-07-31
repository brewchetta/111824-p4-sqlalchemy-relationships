#!/usr/bin/env python3

from app import app
from models import db, Deli
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")
        d1 = Deli(name="Deli One")

        db.session.add_all( all the delis as a list )
        db.session.commit()

        print("Seeding complete!")
