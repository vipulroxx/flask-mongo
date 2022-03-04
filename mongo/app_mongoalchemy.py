from server_mongoalchemy import Author, Book
from flask import Flask, request

app = Flask(__name__)

@app.route("/update")
def update():
    a = request.args.get('author')
    b = request.args.get('book')
    y = request.args.get('year')
    author = Author(name=a)
    book = Book(title=b, author=author, year=int(y))
    author.save()
    book.save()
    return 'Added'

@app.route("/author", methods=["GET", "POST"])
def author_query():
    a = request.args.get('name')
    author = Author.query.filter(Author.name == a).first()
    try:
       return author.name
    except:
       return ("Author not found")

@app.route("/book", methods=["GET", "POST"])
def book_query():
    b = request.args.get('title')
    book = Book.query.filter(Book.title == b).first()
    try:
       return book.title
    except:
       return ("Book not found")

@app.route("/author/update/", methods=["GET", "POST"])
def update_authorname():
    a = request.args.get('original')
    b = request.args.get('new')
    author = Author.query.filter(Author.name == a).first()
    author.name = b 
    author.save()
    return 'Saved'

@app.route("/author/delete", methods=["GET", "POST"])
def delete_author():
    a = request.args.get('author')
    remove_author = Author.query.filter(Author.name == a).first()
    remove_author.remove()
    return 'Removed'
