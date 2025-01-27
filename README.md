# Flask SQLAlchemy Relationships

## Learning Goals

- Has many & belongs to relationships in sqlalchemy

- Using the association_proxy for many to many relationships

- Building join tables

## Getting Started

Fork and clone the repository. Inside the repo run

```bash
pipenv install
pipenv shell
cd server
```

You can find your `models.py` file inside the `server` directory.

## Workflow

Create your models inside `models.py`. Once complete, you'll need to import them inside `app.py` in order to make things work correctly.

Once your basic models are complete, run these commands in order to create and upgrade your database:

```bash
flask db init
flask db migrate -m "message goes here"
flask db upgrade
```

If you want to add new models, change a column, or made a mistake, you can always edit `models.py` and then run:

```bash
flask db migrate -m "message about changes here"
flask db upgrade
```

This will generate a new migration for your database with the necessary changes.

You may now interact with your models by entering the flask shell:

```bash
flask shell
```

## One to Many Relationship

We can start by creating a one to many relationship between two models. First we need to decide which is the one and which is the many. The many always gets the foreign key.

You can add a foreign key column with:

```python
raccoon_id = db.Column(db.Integer, db.ForeignKey('raccoons_table.id'))
```

The foreign key is the only time we need to run `flask db migrate` and `flask db upgrade`. This will allow a foreign key to exist in the table.

Next we set up a relationship. If we have two models, `Trashcan` and `Raccoon` we'll need to next create our relationship attributes.

```python
class Raccoon(db.Model):

    # stuff goes here ####################

    trashcans = db.relationship('Trashcan', back_populates='raccoon')

class Trashcan(db.Model):

    # stuff goes here ####################

    raccoon = db.relationship('Raccoon', back_populates='trashcans')
```

You'll notice the name for one attribute is the `back_populates` for the other. Additionally, the first argument for the relationship will always be the string name for the other model.

This will allow us to do two things:

```python
# get a raccoon named Rocky
rocky = Raccoon.query.where(Raccoon.name == 'Rocky Raccoon').first()

rocky.trashcans 
# this will return a list of trashcans with this raccoon's id as their foreign key
```

```python
# get a trashcan
trashcan_one = Trashcan.query.first()

trashcan_one.raccoon 
# this will return the raccoon that has claimed the trashcan 
# a.k.a. the raccoon related that matches the foreign key
```

## Many to Many

A many to many relationship is truthfully two one to many relationships with an extra step. Using the example above, we might say that a business has many trashcans and therefore many raccoons through their trashcans.

```
Business --< Trashcan >-- Raccoon
```

The trashcan would then be considered the JOIN TABLE. A business can track all the raccoons it has through the Trashcan model.

To set this up we first create two one to many relationships.

```python
class Trashcan(db.Model):

    # other attributes go here ##########

    business_id = db.Column(db.Integer, db.ForeignKey('businesses_table.id'))
    business_id = db.Column(db.Integer, db.ForeignKey('raccoons_table.id'))

    business = db.relationship('Business', back_populates='trashcans')
    raccoon = db.relationship('Raccoon', back_populates='trashcans')

class Business(db.Model):

    # other attributes go here ##########
    
    trashcans = db.relationship('Trashcan', back_populates='business')

class Raccoon(db.Model):

    # other attributes go here ##########

    trashcans = db.relationship('Trashcan', back_populates='raccoon')
```

Once those relationships are created we can add an `association_proxy` which creates an additional attribute that accesses the next step in the relationship.

```python
from sqlalchemy.ext.associationproxy import association_proxy

class Business(db.Model):

    # other attributes go here ##########
    
    trashcans = db.relationship('Trashcan', back_populates='business')

    raccoons = association_proxy('trashcans', 'raccoon')
```

The arguments for the `association_proxy` can be thought of as steps. The first step is the attribute that goes to `trashcans` and the second step is once we're in the `Trashcan` model how do we get to the `Raccoon`? In this case the `Trashcan` model has a `raccoon` attribute so we use that as the second attribute.