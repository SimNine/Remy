from dataclasses import dataclass
import uuid

import peewee

db = peewee.SqliteDatabase("remy.db")

class Recipe(peewee.Model):
    name = peewee.CharField()
    description = peewee.CharField()

    class Meta:
        database = db

class Ingredient(peewee.Model):
    name = peewee.CharField()
    recipe = peewee.ForeignKeyField(Recipe, backref="ingredients", null=True)
    units = peewee.CharField()

    class Meta:
        database = db

class RecipeToIngredient(peewee.Model):
    recipe = peewee.ForeignKeyField(Recipe, backref="recipe_to_ingredient")
    ingredient = peewee.ForeignKeyField(Ingredient, backref="recipe_to_ingredient")
    quantity = peewee.FloatField()

    class Meta:
        database = db

class RecipeToStep(peewee.Model):
    recipe = peewee.ForeignKeyField(Recipe, backref="recipe_to_step")
    step = peewee.CharField()
    order = peewee.IntegerField()  # 1-indexed

    class Meta:
        database = db