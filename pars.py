# import requests
# from bs4 import BeautifulSoup as bs
# import time

# def get_search_results(search_term):
#     base_url = "https://rezka.ag/search/?do=search&subaction=search&q="
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     data = {
#         'q': search_term,
#         'scf': 'fx',
#         'search_start': 0,
#         'do': 'search',
#         'subaction': 'search',
#         'years_ot': 1902,
#         'years_do': 2024,
#         'kpi_ot': 1,
#         'kpi_do': 10,
#         'imdb_ot': 1,
#         'imdb_do': 10,
#         'sort_name': '',
#         'undefined': 'asc',
#         'sort_date': '',
#         'sort_favorite': '',
#         'simple': 1
#     }

#     response = requests.post(base_url, headers=headers, data=data)
#     soup = bs(response.text, 'html.parser')

#     navigation_div = soup.find("div", class_="b-navigation")
#     if navigation_div:
#         page_count = navigation_div.find_all("a")[-2].text
#         for i in range(1, int(page_count) + 1):
#             url = f"https://rezka.ag/search/?do=search&subaction=search&q={search_term}&page={i}"
#             r = requests.get(url=url, headers=headers)
#             soup_page = bs(r.text, 'html.parser')  # Парсим новую страницу

#             all_films = soup_page.find("div", class_="b-content__inline_items")
#             new_list = [str(i) for i in all_films]

#             with open(f"ukr_net_links{i}.html", "w") as file:
#                 for item in new_list:
#                     file.write("\n" + item)

#             time.sleep(2)
#             print(new_list)
#     else:
#         print("Навігаційний блок не знайдено.")

# def main():
#     search_term = input("Введіть слово для пошуку: ")
#     get_search_results(search_term)

# if __name__ == '__main__':
#     main()










# # from bs4 import BeautifulSoup
# # import requests

# # url = '' 
# # page = requests.get(url)
# # print(page.status_code)

# # soup = BeautifulSoup(page.content, "html.parser")

# # main_id = soup.find(id="main")
# # links_a_main = main_id.find_all("a")

# # with open("ukr_net_links.txt", "w", encoding="utf-8") as file:
# #     for link in links_a_main:
# #         # Преобразовываем ссылку в строку с помощью prettify() и записываем в файл
# #         file.write(link.prettify() + "\n")



# # from bs4 import BeautifulSoup
# # import requests
# # import json

# # url = '' 
# # page = requests.get(url)
# # response = requests.get(url)
# # print(page.status_code)

# # soup = BeautifulSoup(page.content, "html.parser")

# # main_id = soup.find(id="main")
# # links_a_main = main_id.find_all("a")

# # new_list = [str(i) for i in links_a_main]

# # with open ("ukr_net_links.txt", "w", encoding='utf-8') as file:
# #         for i in new_list:
# #             file.write("\n" + i)



# # название 
# # рік 
# # описание 
# # картінка 