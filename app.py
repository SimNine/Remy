from flask import Flask, request, redirect

from recipe import Ingredient, RecipeToIngredient, db, Recipe

db.connect()
db.create_tables([Recipe, Ingredient, RecipeToIngredient])

app = Flask(__name__)

@app.route("/")
def route_main_page():
    return (
        f"<p>Hello, World!</p>" +
        f"<div>" +
        f"<h2>Recipes</h2>" +
        "".join([
            f"<div>{recipe.name}</div>"
            for recipe in Recipe.select()
        ]) +
        f"</div>" +
        f"<p>Add New Recipe:</p>" +
        f"<form method='post' action='/recipe_add'>" +
        f"<input type='text' name='name' placeholder='Name'>" +
        f"<input type='text' name='description' placeholder='Description'>" +
        f"<input type='text' name='ingredients' placeholder='Ingredients'>" +
        f"<input type='text' name='steps' placeholder='Steps'>" +
        f"<input type='submit'>" +
        f"</form>"
    )

@app.route("/recipe_add")
def route_recipe_add():
    name = request.form["name"]
    description = request.form["description"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]

    recipe_new = Recipe(
        name=name,
        description=description,
    )
    recipe_new.save()

    # recipe_file = Path("recipes") / f"{recipe.id}.json"
    # with recipe_file.open("w") as file:
    #     json.dump(recipe.to_json(), file, indent=2)

    return redirect("/")