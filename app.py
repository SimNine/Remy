from flask import Flask, request, redirect

from recipe import Ingredient, RecipeToIngredient, db, Recipe

db.connect()
db.create_tables([Recipe, Ingredient, RecipeToIngredient])

app = Flask(__name__)

current_recipe = None

@app.route("/")
def route_main_page():
    return (
        f"<div>" +
        f"<h2>Recipes</h2>" +
        "".join([
            f"<div><a  href='recipe_view/{recipe.name}'>{recipe.name}</a></div>"
            for recipe in Recipe.select()
        ]) +
        f"</div>" +
        f"<h2>Add New Recipe:</h2>" +
        f"<form method='post' action='/recipe_add'>" +
        f"<div><input type='text' name='name' placeholder='Name'></div>" +
        f"<div><input type='text' name='description' placeholder='Description'></div>" +
        f"<div><input type='text' name='ingredients' placeholder='Ingredients'></div>" +
        f"<div><input type='text' name='steps' placeholder='Steps'></div>" +
        f"<div><input type='submit'></div>" +
        f"</form>"
    )

@app.route("/recipe_view/<name>")
def route_view_recipe(name: str):
    recipe: Recipe = Recipe.get(Recipe.name == name)

    def render_ingredient_list(recipe: Recipe, indentation: str = ""):
        return (
            f"<div>" +
            "".join([
                f"<div>{indentation}{ingredient.name}</div>"
                for ingredient in recipe.ingredients
            ]) +
            f"</div>"
        )

    return (
        f"<div>" +
        f"<h2>{recipe.name}</h2>" +
        f"<h3>Description:</h3>" +
        f"<p>{recipe.description}</p>" +
        f"<h3>Ingredients:</h3>" +
        render_ingredient_list(recipe) +
        f"</div>"
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
