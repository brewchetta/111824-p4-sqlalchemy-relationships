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

## Create

In our case we've created two models, `Deli` and `Hamburger`. If we want to create a new instance of a `Deli` we can do that in the shell by typing:

```python
new_deli = Deli(name="Bob's Deli", location="Staten Island")
```

The new `Deli` instance hasn't been added or committed as a database row yet so we'll next need to run:

```python
db.session.add(new_deli)
db.session.commit()
```

The workflow here is similar to adding and committing to github. Technically you can make multiple changes and add them all before running a single `db.session.commit()`. The `Deli` should now be in our database.

## Read

To see every `Deli` in our database we can read it with:

```python
Deli.query.all()
```

The `Deli.query` will run specific SQL queries on our database and can be amended in certain ways. The final method `.all()` determines how many items we get back. With `.all()` we will always get back a list of the `Deli` instances whereas `.first()` will just get back a single `Deli`.

We can amend our statement to find a `Deli` with a specific id or name:

```python
Deli.query.where(Deli.id == 1).first()
Deli.query.filter(Deli.name == "Bob's Deli").first()
```

The `.where` and `.filter` can be used interchangeably here. This will allow us to find the first `Deli` with an id of 1 or a name of "Bob's Deli".

## Update

There are multiple ways to update a `Deli` but the easiest might be to simply change an attribute and commit it.

```python
bobs_deli = Deli.query.where(Deli.name == "Bob's Deli").first()
bobs_deli.location = "Queens"
bobs_deli.name = "Bob's Deli for Raccoons"
db.session.commit()
```

Once all changes have been made you can simply run the `db.session.commit()` function and they'll immediately get added to the database.

## Delete

Delete is fairly simple. If we've decided we need to delete an item from the database we run two commands:

```python
db.session.delete(bobs_deli)
db.session.commit()
```

Once done, "Bob's Deli" should no longer exist in the database. Most often you'll be deleting by id so a more full example would look like this:

```python
deli_to_delete = Deli.query.where(Deli.id == 1).first()
db.session.delete(deli_to_delete)
db.session.commit()
```
