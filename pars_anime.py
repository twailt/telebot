import requests
from bs4 import BeautifulSoup as bs

def get_search_results(search_term, page_number=1):
    base_url = "https://anime-portal.su/search/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_links = []

    url = f"{base_url}{search_term}/page/{page_number}"
    response = requests.get(url=url, headers=headers, timeout=40)
    
    try:
        response.raise_for_status() 
        soup = bs(response.text, 'html.parser')
        content_divs = soup.find_all("div", class_="col-content")

        for div in content_divs:
            links = div.find_all("a")
            for link in links:
                href_value = link.get("href")
                all_links.append(href_value)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return all_links


