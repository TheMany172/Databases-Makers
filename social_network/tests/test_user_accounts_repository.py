from lib.user_accounts_repository import *
from lib.user_accounts import *
from lib.database_connection import *

"""
call all 
"""
def test_get_all(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserAccountsRepository(db_connection) 
    
    accounts = repository.all() 
    assert accounts == [
        UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com'),
        UserAccounts(2, 'neonsprinkle', 'neonsprinkle@real.com')
    ]


"""
wanting to call find useraccounts with an id
"""

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountsRepository(db_connection)
    result = repository.find(2)
    assert result == UserAccounts(2, 'neonsprinkle', 'neonsprinkle@real.com')

"""
create function - using INSERT
"""

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountsRepository(db_connection)
    repository.create('Adder172', 'adder172@real.com')
    accounts = repository.all()
    assert accounts == [
        UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com'),
        UserAccounts(2, 'neonsprinkle', 'neonsprinkle@real.com'),
        UserAccounts(3, 'Adder172', 'adder172@real.com')
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountsRepository(db_connection)
    repository.delete(2)
    accounts = repository.all()
    assert accounts == [
        UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    ]

def test_delete_both(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountsRepository(db_connection)
    repository.delete(2)
    accounts = repository.all()
    assert accounts == [
        UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    ]
    repository.delete(1)
    accounts = repository.all()
    assert accounts == []