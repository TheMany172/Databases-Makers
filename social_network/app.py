from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository
# from lib.AlbumRepository import *
# from lib.RecipeRepository import *
from lib.posts_repository import *
from lib.user_accounts_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

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

users = UserAccountsRepository(connection)
for user in users.all():
    print (user)

posts = PostsRepository(connection)
for post in posts.all():
    print (post)