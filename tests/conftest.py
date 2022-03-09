import pytest
import flask_mongoalchemy as mongoalchemy
from tests.helpers import _make_todo_author_document, _make_todo_book_document
from mongo import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"MONGOALCHEMY_DATABASE": 'testing', "TESTING" : True, })
    return app

@pytest.fixture
def setup_author_todo(app):
    db = mongoalchemy.MongoAlchemy(app)
    Todo = _make_todo_author_document(db)
    return Todo

@pytest.fixture
def setup_book_todo(app):
    db = mongoalchemy.MongoAlchemy(app)
    Todo = _make_todo_book_document(db)
    return Todo

@pytest.fixture
def teardown_author_todo(app):
    db = mongoalchemy.MongoAlchemy(app)
    Todo = _make_todo_author_document(db)
    for todo in Todo.query.all():
        todo.remove()
    return Todo

@pytest.fixture
def teardown_book_todo(app):
    db = mongoalchemy.MongoAlchemy(app)
    Todo = _make_todo_book_document(db)
    for todo in Todo.query.all():
        todo.remove()
    return Todo

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
