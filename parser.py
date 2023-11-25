import requests
from bs4 import BeautifulSoup

def get_latest_news(urls):
    news = []

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Ваш код для извлечения новостей из HTML-кода
            # news.append(...)

        except Exception as e:
            print(f"Ошибка при обработке URL {url}: {e}")

    return news