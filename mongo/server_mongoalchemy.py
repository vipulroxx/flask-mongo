from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from marshmallow import Schema, fields, post_load, validate

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'library'

db = MongoAlchemy(app)

class Author(db.Document):
    name = db.StringField()

class AuthorSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))

@post_load
def make_author(self, data, **kwargs):
    return Author(**data)

class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField()

class BookSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1))
    author =  fields.Nested(AuthorSchema)
    year = fields.Int(required=True) 

@post_load
def make_book(self, data, **kwargs):
    return Book(**data)
