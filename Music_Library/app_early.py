from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.AlbumRepository import *



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# # Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# # Retrieve all Albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

