from lib.AlbumRepository import *
from lib.Album import *


"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

def test_get_all_albums(db_connection): 
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumRepository(db_connection) 

    album = repository.all() 

    # Assert on the results
    assert album == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]


"""
wanting to call find on AlbumRepository with an id so that we can 
that artist back
"""

def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(3)
    assert result == Album(3, "Waterloo", 1974, 2)