import pytest

def test_document_save(teardown_author_todo, setup_author_todo, client):
    t = teardown_author_todo
    t = setup_author_todo(name=u'Author name')
    t.save()
    assert t.query.count() == 1

def test_document_remove(teardown_author_todo, setup_author_todo, client):
    t = teardown_author_todo
    t = setup_author_todo(name=u'Author name')
    t.save()
    assert t.query.count() == 1
    t.remove()
    assert t.query.count() == 0
