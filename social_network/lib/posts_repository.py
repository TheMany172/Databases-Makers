from lib.posts import *

class PostsRepository():
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts_list = []
        for row in rows:
            item = Posts(row['id'], row['title'], row['content'], row['number_of_views'], row['user_account_id'])
            posts_list.append(item)
        
        return posts_list


    def find(self, user_id):
        rows = self._connection.execute(
            "SELECT * FROM posts WHERE id = %s", [user_id]
        )
        row = rows[0]
        return Posts(row['id'], row['title'], row['content'], row['number_of_views'], row['user_account_id'])

    def create(self, title, content, number_of_views, user_account_id):
        self._connection.execute(
        "INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES (%s, %s, %s, %s)", [title, content, number_of_views, user_account_id])
        return None
        
    def delete(self, post_id):
        self._connection.execute(
        "DELETE FROM posts WHERE id = %s", [post_id])
        return None

