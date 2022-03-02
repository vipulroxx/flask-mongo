from server_mongoalchemy import Author, Book

mark_pilgrim = Author(name='Mark Pilgrim')
dive = Book(title='Dive into Python', author=mark_pilgrim, year=2004)

mark_pilgrim.save()
dive.save()

author = Author.query.filter(Author.name == 'Mark Pilgrim').first()
book = Book.query.filter(Book.year == 2004).first()

print("Author name: ", author.name)
print("Book title: ", book.title)

#author.name = 'Vipul Sharma'
#author.save()

remove_author = Author.query.filter(Author.name == 'Vipul Sharma').first()
remove_author.remove()
