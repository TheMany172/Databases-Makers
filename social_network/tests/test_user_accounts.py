from lib.user_accounts import *

# init with a username and an email
def test_create_user_account():
    useraccount1 = UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    assert useraccount1.id == 1
    assert useraccount1.username == 'Cupcakes'
    assert useraccount1.email_address == 'ninjacupcake@awesome.com'


    

def test_useraccounts_formatted_nice():
    user1 = UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    assert str(user1) == "UserAccounts(1, Cupcakes, ninjacupcake@awesome.com)"

"""
2 equal entries
"""

def test_useraccounts_are_equal():
    user1 = UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    user2 = UserAccounts(1, 'Cupcakes', 'ninjacupcake@awesome.com')
    
    assert user1 == user2