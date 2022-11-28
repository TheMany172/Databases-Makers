# from lib.database_connection import DatabaseConnection
# # from lib.artist_repository import ArtistRepository

# # from lib.RecipeRepository import *


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # Retrieve all Albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# for album in albums:
#     print(album)

# recipe_repo = RecipeRepository(connection)
# recipes = recipe_repo.all()
# for recipe in recipes:
#     print (recipe)

"""
add in a 'run' 
"""

# file: app.py
from lib.AlbumRepository import *
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
        print ("Welcome to the music library manager!")
        answer = input("What would you like to do? \n 1 - List all albums\n or \n 2 - List all artists \n (type 1 or 2 here -->")

        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        
    

        if answer == '2':
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        else:
            for album in albums:
                print (f"{album.id}: {album.title}")

if __name__ == '__main__':
    
    app = Application()
    app.run()