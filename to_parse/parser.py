import csv
import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
           'accept': '*/*'}
HOST = 'https://auto.ria.com/uk'
FILE = 'cars.csv '


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='proposition_link')

    cars = []
    for item in items:
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text(strip=True)
        else:
            uah_price = "[ None ]"
        usd_price = item.find('span', class_='green').get_text(strip=True)
        if usd_price is not '':
            usd_price = item.find('span', class_='green').get_text(strip=True)
        else:
            usd_price = "[ None ]"
        cars.append({
            'title': item.find('div', class_='proposition_title').get_text(strip=True),
            'link': HOST + item.get('href'),
            'usd_price': usd_price,
            'uah_price': uah_price,
            'city': item.find('span', class_='region').get_text(strip=True),
        })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['марка', 'посилання', 'ціна долар', 'ціна гривня', 'місто'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['uah_price'], item['city']])


def parse():
    my_url = input('Paste URL: ')
    my_url = my_url.strip()
    html = get_html(my_url)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Parse now {page} from {pages_count}')
            html = get_html(my_url, params={'page': page})  #   ?
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        print(len(cars), 'cars')
    else:
        print('Page not found')


parse()