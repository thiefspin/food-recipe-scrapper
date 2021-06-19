import json

from recipe_scrapers import scrape_me
from recipe import Recipe, RecipeEncoder


def find_tags(links):
    tags = []
    for t in links:
        if 'class' in t and 'o-Capsule__a-Tag' in t['class']:
            tags.append(t['title'])
    return tags


def process(url):
    scraper = scrape_me(url)
    return Recipe(
        scraper.title(),
        scraper.total_time(),
        scraper.yields(),
        scraper.ingredients(),
        scraper.instructions(),
        scraper.image(),
        scraper.host(),
        find_tags(scraper.links())
    )


def main():
    output = open("recipes.json", "w")
    with open("sources.txt") as source:
        recipes = list(map(process, source.read().splitlines()))
        json.dump(recipes, output, cls=RecipeEncoder)
    output.close()
    source.close()


if __name__ == "__main__":
    main()
