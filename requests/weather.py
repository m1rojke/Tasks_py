import requests

city = input('Введите город: ')
url = f"https://wttr.in/{city}?format=%l:+%C+%t+%h+%w"

response = requests.get(url)

if response.status_code == 200:
    print(f"Погода в {city}: {response.text}")
else:
    print("Ошибка при получении данных")