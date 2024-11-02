import requests

url = "https://cataas.com/cat"

response = requests.get(url)

if response.status_code == 200:
    with open("random_cat.jpg", "wb") as file:
        file.write(response.content)
    print("Зображення успішно збережено як random_cat.jpg")
else:
    print("Не вдалося завантажити зображення. Статус-код:", response.status_code)
