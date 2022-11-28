from lib.Recipe import *

def test_setup_ok():
    recipe1 = Recipe(1, 'Cupcakes', 20, 4)
    assert recipe1.id == 1
    assert recipe1.names == 'Cupcakes'
    assert recipe1.average_cooking_time == 20
    assert recipe1.rating_one_to_five == 4

"""
nicely format the recipe 
"""

def test_recipes_formatted_nice():
    recipe1 = Recipe(1, 'Cupcakes', 20, 4)
    assert str(recipe1) == "Recipe(1, Cupcakes, 20, 4)"

"""
2 equal entries
"""

def test_recipies_are_equal():
    recipe1 = Recipe(1, 'Cupcakes', 20, 4)
    recipe2 = Recipe(1, 'Cupcakes', 20, 4)
    
    assert recipe1 == recipe2

