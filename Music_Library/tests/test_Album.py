from lib.Album import *

"""
Album constructs with all the self variables 
"""
def test_album_constructs():
    album1 = Album(1, "Ok Computer", 1997, 77)
    assert album1.id == 1
    assert album1.title == "Ok Computer"
    assert album1.release_year == 1997
    assert album1.artist_id == 77

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album1 = Album(1, "Ok Computer", 1997, 77)

    assert str(album1) == "Album(1, Ok Computer, 1997, 77)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Ok Computer", 1997, 77)
    album2 = Album(1, "Ok Computer", 1997, 77)
    
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.

