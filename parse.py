import requests
from bs4 import BeautifulSoup as BS

def create_session(login:str) -> 'requests.session':
    link = 'https://' + login
    session = requests.session()
    session.get(f'https://downloadmusicvk.ru/site/auth?link={link}')
    return session

def get_pages_count(session:'requests.session', url:str) -> int:
    '''Returns count of pages.'''
    soup = BS(session.get(url).text, 'lxml')
    li = soup.find('li', class_='last')
    href = li.find('a').get('href')
    return int(href.split('=')[-1])

def parse_list_page(session:'requests.session', url:str):
    '''Returns the list of songs pages,
        as example: https://downloadmusicvk.ru/audio/list?page=1.
    '''
    soup = BS(session.get(url).text, 'lxml')
    links = soup.find_all('a', class_='btn btn-primary btn-xs download')
    return ['https://downloadmusicvk.ru' + link.get('href') for link in links]
