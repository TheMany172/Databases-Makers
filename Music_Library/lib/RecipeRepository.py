from lib.Recipe import *

class RecipeRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipe_list = []
        for row in rows:
            item = Recipe(row["id"], row["names"], row["average_cooking_time"], row["rating_one_to_five"])
            recipe_list.append(item)
        
        return recipe_list

    def find(self,recipe_id):
        rows = self._connection.execute(
            "SELECT * FROM recipes WHERE id = %s", [recipe_id]
        )
        row = rows[0]
        return Recipe(row["id"], row["names"], row["average_cooking_time"], row["rating_one_to_five"])