'''This program works with web-site https://downloadmusicvk.ru/.
It's downloading music from your vk.com profile.

'''

import os
import time
import requests
from bs4 import BeautifulSoup as BS
import parse
import download
import log

logins = [
    'rita_69_knyaz',
    'n1tr0xs',
]

def benchmark(func):
    def wrapper(login):
        t0 = time.time()
        func(login)
        print('Execution time:', format_time(time.time() - t0))
    return wrapper

@benchmark
def main(login):
    folder = 'D:/VK_downloads/' + login + '/'
    page_url = 'https://downloadmusicvk.ru/audio/list?page={}'

    create_path(folder)
    log_file = log.LogFile(folder)
    print('Downloading songs from', login, 'VK page.')
    session = parse.create_session(login)
    pages_count = parse.get_pages_count(session, page_url.format(1))
    for page_num in range(1, pages_count+1):
        print(f'Processing page {page_num}/{pages_count}.')
        song_pages = parse.parse_list_page(session, page_url.format(page_num))
        for song_page in song_pages:
            download.download_song(folder, song_page, log_file)
    print(f'Songs from {login} VK page downloaded.')

def create_path(path:str):
    '''Creating the path which you give.'''
    if path.endswith('/'):
        path = path[:-1]
    if ('/' not in path) or (os.path.exists(path)):
        return
    create_path(path[:path.rfind('/')])
    os.mkdir(path)

def format_time(seconds:int) -> str:
    res = '{:.0f}h {:.0f}m {:.0f}s'
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    return res.format(hours, minutes, seconds)        

if __name__ == '__main__':
    for login in logins:
        main(login)
