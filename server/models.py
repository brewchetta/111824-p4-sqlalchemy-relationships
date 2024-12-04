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

    hamburgers = db.relationship('Hamburger', back_populates='deli')
    pizzas = db.relationship('Pizza', back_populates='deli')

class Hamburger(db.Model):

    __tablename__ = "hamburgers_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    deli_id = db.Column(db.Integer, db.ForeignKey('delis_table.id'))

    deli = db.relationship('Deli', back_populates='hamburgers')

class Pizza(db.Model):

    __tablename__ = "pizza_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    deli_id = db.Column(db.Integer, db.ForeignKey('delis_table.id'))

    deli = db.relationship('Deli', back_populates='pizzas')

# THIS STUFF IS JUST FOR SEBASTIEN

# class DeliveryTruck(db.Model):

#     __tablename__ = "delivery_truck_table"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
    
#     deliveries = db.relationship('Delivery', back_populates='delivery_truck')

#     delis = association_proxy('deliveries', 'deli')

# class Delivery(db.Model):

#     __tablename__

#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column

#     deli_id
#     delivery_truck_id

#     deli = db.relationship
#     delivery_truck = db.relationship('DeliveryTruck', back_populates='deliveries')