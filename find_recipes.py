import requests
from bs4 import BeautifulSoup

BASE_PAGE = 'https://www.foodnetwork.com/recipes/recipes-a-z'
# ALPHABET = ['123', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#             'u', 'v', 'w', 'xyz']
ALPHABET = ['123']


def write_out(links):
    output = "\n".join(links)
    f = open("source_links.txt", "w")
    f.write(output)
    f.close()

def scrape_page(page_url):
    urls = []
    try:
        page = requests.get(page_url)
        page_contents = BeautifulSoup(page.content, "html.parser")
        page_elements = page_contents.find(class_="l-Columns l-Columns--2up")
        links = page_elements.find_all("a")
        for link in links:
            link_url = link["href"]
            full_url = 'https:' + link_url
            urls.append(full_url)
    except:
        print('end of pages reached')
        return False
    print('Found ' + str(len(urls)) + ' for page ' + str(page_url))
    return urls


def main():
    all_urls = []

    for letter in ALPHABET:
        for i in range(1, 500):
            result = scrape_page(BASE_PAGE + '/' + letter + '/p/' + str(i))
            if result is False:
                break
            all_urls = all_urls + result
    print(len(all_urls))
    write_out(all_urls)


if __name__ == "__main__":
    main()
