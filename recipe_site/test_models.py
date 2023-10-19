from django.test import TestCase
from .models import Post, Drink


class TestPostModel(TestCase):
    def test_recipe_name_is_string(self):
        post = Post(recipe_name="Recipe Name")
        self.assertEqual(str(post), post.recipe_name)


class TestDrinkModel(TestCase):
    def test_drink_name_is_string(self):
        drink = Drink(drink_name="Drink Name")
        self.assertEqual(str(drink), drink.drink_name)
