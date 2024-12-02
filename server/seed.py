from app import app
from models import db, Deli

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        # seed delis here...

        print("Seeding complete!")
