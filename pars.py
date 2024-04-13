import requests
from bs4 import BeautifulSoup as bs

def get_search_results(search_term, page=1):
    base_url = "https://rezka.ag/search/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_links = []
    page = 1
    while True:
        url = f"{base_url}?do=search&subaction=search&q={search_term}&page={page}"
        response = requests.get(url=url, headers=headers, timeout=40)

        soup = bs(response.text, 'html.parser')

        all_films = soup.find_all("div", class_="b-content__inline_item")
        if not all_films:
            break

        for film in all_films:
            link = film.find("a")["href"]
            all_links.append(link)

        page += 1

    return all_links
