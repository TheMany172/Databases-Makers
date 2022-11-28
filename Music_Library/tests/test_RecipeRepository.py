from lib.RecipeRepository import *
from lib.Recipe import *


"""
call all recipes with seed data?
"""

def test_get_all_recipes(db_connection): 
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection) 

    recipe = repository.all() 

    # Assert on the results
    assert recipe == [
        Recipe(1, 'Cupcakes', 20, 4),
        Recipe(2, 'browniest cookies', 30, 5),
        Recipe(3, 'spag cake bake', 50, 4),
        Recipe(4, 'veggie curry', 70, 4),
        Recipe(5, 'spicy wraps', 20, 3),
    ]

"""
wanting to call find RecipeRepository with an id
"""

def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.find(3)
    assert result == Recipe(3, 'spag cake bake', 50, 4)