import pytest

def test_index(client):
    response = client.get("/users/index")
    assert b"<h1>USER CRUD</h1>" in response.data
    assert b"CREATE" in response.data
    assert b"GET" in response.data
    assert b"UPDATE" in response.data
    assert b"DELETE" in response.data

@pytest.mark.parametrize(('author', 'book', 'year'), (('Author 1', 'Book 1', 1111),))
def test_create(teardown_book_todo, setup_book_todo, client, author, book, year):
    response = client.post('/users/create', data={'author':author, 'book':book, 'year': year})
    assert b'Saved' in response.data
    
@pytest.mark.parametrize(('author'), (('Author 1'),))
def test_get(teardown_book_todo, setup_book_todo, client, author):
    response = client.post('/users/book/get', data={'author':author})
    assert client.get('/users/book/get').status_code == 200
    assert b'Book 1' in response.data

@pytest.mark.parametrize(('author', 'title', 'year'), (('Author 2', 'Book 1', 2222),))
def test_update(teardown_book_todo, setup_book_todo, client, author, title, year):
    response = client.post('/users/book/update', data={'author':author, 'title':title, 'year': year}, follow_redirects=False)
    if 300 <= response.status_code < 400:
        response = client.get(response.headers['Location'], headers={
            "Referer": 'http://localhost/users/book/update'
        })
    assert b'Author' in response.data

@pytest.mark.parametrize(('title'), (('Book 1'),))
def test_delete(teardown_book_todo, setup_book_todo, client, title):
    response = client.post('/users/book/delete', data={'title':title})
    assert b'Deleted' in response.data
