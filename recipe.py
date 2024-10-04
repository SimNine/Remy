from dataclasses import dataclass
import uuid

import peewee

db = peewee.SqliteDatabase("remy.db")

class Recipe(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()
    # steps: list[str]

    class Meta:
        database = db

class Ingredient(peewee.Model):
    name = peewee.CharField()
    recipe = peewee.ForeignKeyField(Recipe, backref="ingredients")

    class Meta:
        database = db

class RecipeToIngredient(peewee.Model):
    recipe = peewee.ForeignKeyField(Recipe, backref="recipe_to_ingredient")
    ingredient = peewee.ForeignKeyField(Ingredient, backref="recipe_to_ingredient")

    class Meta:
        database = db