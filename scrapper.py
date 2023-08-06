import json
from typing import TextIO

from recipe_scrapers import scrape_me
from recipe import Recipe, RecipeEncoder


def find_tags(links):
    tags = []
    for t in links:
        if 'class' in t and 'o-Capsule__a-Tag' in t['class']:
            tags.append(t['title'])
    return tags


def process(url):
    print(url)
    try:
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
    except:
        return False


def main():
    output: TextIO = open("recipes_1.json", "w")
    with open("source_links.txt") as source:
        recipes = []
        lines = source.read().splitlines()
        total_count = len(lines)
        count = 0
        for line in lines:
            count = count + 1
            result = process(line)
            print(str(count) + ' of ' + str(total_count) + ' processed')
            if result is not False:
                recipes.append(result)
        # recipes = list(map(process, source.read().splitlines()))
        json.dump(recipes, output, cls=RecipeEncoder)
        print('Found ' + str(len(recipes)) + ' recipes')
    output.close()
    source.close()


if __name__ == "__main__":
    main()
