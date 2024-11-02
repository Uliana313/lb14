import requests
from bs4 import BeautifulSoup
import json

def count_keywords(url, keywords):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    keyword_counts = {keyword: 0 for keyword in keywords}

    for keyword in keywords:
        for tag in soup.find_all(string=lambda text: keyword in text):
            keyword_counts[keyword] += 1

    return keyword_counts

def main():

    # Вводимо список ключових слів
    keywords = input("Введіть ключові слова, розділені комами: ").split(',')

    # Вводимо список URL
    urls = input("Введіть URLs веб-сторінок, розділені комами: ").split(',')

    # Збираємо дані про кількість ключових слів
    results = {}
    for url in urls:
        results[url] = count_keywords(url, keywords)

    # Зберігаємо результати у JSON файл
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print("Результати записані у файл 'results.json'")

if __name__ == "__main__":
    main()