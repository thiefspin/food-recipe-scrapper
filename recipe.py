import json
from json import JSONEncoder


class Recipe:
    def __init__(self, title, total_time, servings, ingredients, instructions, image, source, tags):
        self.title = title
        self.total_time = total_time
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions
        self.image = image
        self.source = source
        self.tags = tags

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class RecipeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
