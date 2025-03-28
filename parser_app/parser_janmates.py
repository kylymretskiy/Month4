import requests
from bs4 import BeautifulSoup

#Строго главную страницу (index) файл
URL = "https://www.janmates.com"

#HEADERS - это внутренние данные сайта указываем для того что мы не являемся роботом
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
}

#1 создание запроса
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 Получение данных через html (Консоль разработчика)
def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="product-preview__content")
    janmates_list = []
    for item in items:
        title = item.find("div", class_='product-preview__title').get_text(strip=True)
        janmates_list.append({
            "title": title,
        })
    return janmates_list

#3 Функционал парсинга и объединение 2х функций в 1
def parsing_janmates():
    response = get_html(URL)
    if response.status_code == 200:
        janmates_list2 = []
        for page in range(1,2):
            response = get_html("https://www.janmates.com/collection/knigi", params={'page': page})
            janmates_list2.extend(get_data(response.text))
        return  janmates_list2
    else:
        raise Exception("error in parsing")

# print(parsing_janmates())