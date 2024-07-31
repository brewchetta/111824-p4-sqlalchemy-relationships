#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Deli #, Hamburger

# this is our flask application!
app = Flask(__name__)
# the config for the uri determines the name of the database we'll use
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# the setup for migrate and the init_app connects everything together with alembic (the migration tool)
migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello World"

# @app.post('/delis')
# def create_deli():
#     newdeli = Deli(xxxx)
#     db.session.add(newdeli)
#     db.session.commit()

# @app.get('/hamburgers')
# def all_hamburgers():
#     return jsonify( Hamburger.query.all() )

if __name__ == '__main__':
    app.run(port=5555, debug=True)
