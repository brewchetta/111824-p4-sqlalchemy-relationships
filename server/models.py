from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Album ---< Songs

class Album(db.Model):
    
    __tablename__ = "albums_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    artist = db.Column(db.String)

    songs = db.relationship('Song', back_populates='album')


class Song(db.Model):
    
    __tablename__ = "songs_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    length = db.Column(db.Float)
    # foreign key
    album_id = db.Column(db.Integer, db.ForeignKey("albums_table.id") )

    album = db.relationship('Album', back_populates='songs')


# #########################################################################

# Owner ---< Dog

class Owner(db.Model):
    
    __tablename__ = "owners_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    dogs = db.relationship('Dog', back_populates='owner')


class Dog(db.Model):
    
    __tablename__ = "dogs_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tail = db.Column(db.Boolean)
    breed = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners_table.id"))

    owner = db.relationship('Owner', back_populates='dogs')

# #########################################################################

# Magazine --< Article >-- Author

class Magazine(db.Model):
    
    __tablename__ = 'magazines_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # RELATIONSHIP
    articles = db.relationship('Article', back_populates='magazine')

    # MANY TO MANY RELATIONSHIP
    authors = association_proxy('articles', 'author')

    def hello(self):
        return "HELLO!"


class Author(db.Model):

    __tablename__ = 'authors_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # RELATIONSHIP
    articles = db.relationship('Article', back_populates='author')

    # MANY TO MANY RELATIONSHIP
    magazines = association_proxy('articles', 'magazine')


class Article(db.Model):

    __tablename__ = 'articles_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # FOREIGN KEYS
    magazine_id = db.Column(db.Integer, db.ForeignKey('magazines_table.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('authors_table.id'))

    # RELATIONSHIPS
    magazine = db.relationship('Magazine', back_populates='articles')
    author = db.relationship('Author', back_populates='articles')