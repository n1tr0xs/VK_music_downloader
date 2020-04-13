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


def main(login):
    folder = 'downloads/' + login + '/'
    page_url = 'https://downloadmusicvk.ru/audio/list?page={}'

    create_folder(folder)
    log_file = log.LogFile(folder)
    
    session = parse.create_session(login)
    pages_count = parse.get_pages_count(session, page_url.format(1))
    for page_num in range(1, pages_count+1):
        print(f'Processing page #{page_num}.')
        song_pages = parse.parse_list_page(session, page_url.format(page_num))
        for song_page in song_pages:
            download.download_song(folder, song_page, log_file)
    print('Songs downloaded.')

def create_folder(folder:str):
    try: os.mkdir(folder.split('/')[0])
    except: pass

    try: os.mkdir(folder)
    except: pass

def format_time(seconds:int) -> str:
    res = '{:.0f}h {:.0f}m {:.0f}s'
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    return res.format(hours, minutes, seconds)


# Starting the programm
login = 'n1tr0xs'
t0 = time.time()
main(login)
print('Execution time:', format_time(time.time() - t0))
