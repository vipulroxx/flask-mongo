def _make_todo_author_document(db):
    class AuthorTodo(db.Document):
        name = db.StringField()
    return AuthorTodo

def _make_todo_book_document(db):
    class BookTodo(db.Document):
        title = db.StringField()
        author = db.StringField()
        year = db.IntField()
    return BookTodo
