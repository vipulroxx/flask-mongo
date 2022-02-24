from server_mongoalchemy import Author, Book

mark_pilgrim = Author(name='Mark Pilgrim')
dive = Book(title='Dive into Python', author=mark_pilgrim, year=2004)

mark_pilgrim.save()
dive.save()
