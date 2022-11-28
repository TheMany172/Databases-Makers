from lib.posts_repository import *
from lib.posts import *
from lib.database_connection import *

"""
call all 
"""
def test_get_all(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection) 
    
    posts = repository.all() 
    assert posts == [
        Posts(1,'You are rubbish', 'whatever', 5, 2),
        Posts(2,'I disagree', 'Actually you are really nice and i like you <3', 5, 1)
    ]


"""
wanting to call find posts with an id
"""

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    result = repository.find(2)
    assert result == Posts(2,'I disagree', 'Actually you are really nice and i like you <3', 5, 1)

"""
create function - using INSERT
"""

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    repository.create('I agree', 'you really are rubbish', 10, 2)
    posts = repository.all()
    assert posts == [
        Posts(1,'You are rubbish', 'whatever', 5, 2),
        Posts(2,'I disagree', 'Actually you are really nice and i like you <3', 5, 1),
        Posts(3, 'I agree', 'you really are rubbish', 10, 2)
    ]
    

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Posts(1,'You are rubbish', 'whatever', 5, 2)
    ]

def test_delete_both(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Posts(1,'You are rubbish', 'whatever', 5, 2)
    ]
    repository.delete(1)
    posts = repository.all()
    assert posts == []