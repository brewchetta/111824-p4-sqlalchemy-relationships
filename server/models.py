from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Deli(db.Model):
    
    __tablename__ = "delis_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    has_bodega_cat = db.Column(db.Boolean)

class Hamburger(db.Model):

    __tablename__ = "hamburgers_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)