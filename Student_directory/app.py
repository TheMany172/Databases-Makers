from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
        print("Welcome to the music library manger!")
    def run_artist(self):
        artist_repository = ArtistRepository(self._connection)
        for artist in artist_repository.all():
            print(f"{artist.id}: {artist.name} ({artist.genre})")
    def run_album(self):
        album_repository = AlbumRepository(self._connection)
        for album in album_repository.all():
            print(f"{album.id} - {album.title}")


if __name__ == '__main__':
    app = Application()
    print("What would you like to do?\n 1 - List all albums\n 2 - List all artists\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        app.run_album()
    elif choice == "2":
        app.run_artist()
    else:
        print('Pick a number between 1 or 2!')