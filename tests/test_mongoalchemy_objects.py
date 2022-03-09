import pytest
import flask_mongoalchemy as mongoalchemy
from mongoalchemy import fields

def test_objects_fields():
    db = mongoalchemy.MongoAlchemy()
    for key in dir(fields):
        assert hasattr(db, key), "should have the %s attribute" % key
    assert hasattr(db, 'DocumentField'), "should have the DocumentField attribute"
