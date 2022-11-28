from lib.posts import *

# init with a username and an email
def test_create_post_with_properties():
    post1 = Posts(1, 'You are rubbish', 'whatever', 5, 2)
    assert post1.id == 1
    assert post1.title == 'You are rubbish'
    assert post1.content == 'whatever'
    assert post1.number_of_views == 5
    assert post1.user_account_id == 2
    

def test_useraccounts_formatted_nice():
    post1 = Posts(1, 'You are rubbish', 'whatever', 5, 2)
    assert str(post1) == "Posts(1, You are rubbish, whatever, 5, 2)"

"""
2 equal entries
"""

def test_posts_are_equal():
    post1 = Posts(1, 'You are rubbish', 'whatever', 5, 2)
    post2 = Posts(1, 'You are rubbish', 'whatever', 5, 2)
    
    assert post1 == post2
