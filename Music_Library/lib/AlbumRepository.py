from lib.Album import *

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all Albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self,album_id):
        rows = self._connection.execute(
            "SELECT * FROM albums WHERE id = %s", [album_id]
        )
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])