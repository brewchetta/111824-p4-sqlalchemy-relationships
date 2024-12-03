from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# the metadata here creates foreign key naming conventions in the database
# you generally won't have to set this up
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# this sets up the database connection
db = SQLAlchemy(metadata=metadata)

# this will eventually become our Deli model
class Deli(db.Model):
    
    __tablename__ = "delis_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    has_ice_cream = db.Column(db.Boolean)
    bacon_egg_cheese = db.Column(db.Boolean)
    bodega_cat = db.Column(db.Boolean)