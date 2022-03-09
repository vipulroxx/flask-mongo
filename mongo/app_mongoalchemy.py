import pprint
from mongo.server_mongoalchemy import Author, Book, AuthorSchema, BookSchema
from flask import (Flask, request, Blueprint, flash, g, redirect, render_template, url_for)
from marshmallow import ValidationError

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route("/index", methods=["GET", "POST"])
def index():
    return render_template('users/index.html')

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        a = request.form['author']
        b = request.form['book']
        y = request.form['year']
        e = 0
        author_schema = AuthorSchema()
        try:
            author = author_schema.load({"name":a})
        except ValidationError as err:
            for messages in err.messages.values():
                for message in messages:
                    flash(message)
            e += 1
        book_schema = BookSchema()
        try:
            book = book_schema.load({"title":b, "author": {"name": a}, "year":int(y)})
        except ValidationError as err:
            flash(message.pop(0) for message in err.messages.values())
            e += 1
        if e == 0:
            author_res = Author(name=a)
            author_res.save()
            book_res = Book(title=b, author=author_res, year=int(y))
            book_res.save()
            flash('Saved')
    return render_template('users/create.html') 

@bp.route("/book/get", methods=["GET", "POST"])
def get():
    if request.method == "POST":
        a = request.form['author']
        book_schema = BookSchema(many=True)
        try:
            book = Book.query.filter(Book.author.name == a).all()
            book_result = book_schema.dump(book)
            return render_template('users/get.html', books=book_result) 
        except:
            flash("Book not found")
            return render_template('users/get.html') 
    return render_template('users/get.html') 

@bp.route("/book/update/", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        a = request.form['author']
        b = request.form['title']
        y = request.form['year']
        book = Book.query.filter(Book.title == b).first()
        book.title = b 
        book.author.name = a
        book.year = int(y)
        book.save()
        flash("Saved")
    return render_template('users/update.html') 

@bp.route("/book/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        b = request.form['title']
        book = Book.query.filter(Book.title == b).first()
        book.remove()
        flash('Deleted')
    return render_template('users/delete.html')
