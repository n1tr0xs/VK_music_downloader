import requests
from bs4 import BeautifulSoup as BS

def download_song(folder:str, url:str, log_file:list):
    '''Downloads the song on given url.'''
    log_url = '&'.join(url.split('&')[1:3])
    if log_url in log_file.downloaded: # exit if already downloaded
        return

    soup = BS(requests.get(url).text, 'lxml')
    song_name = ' '.join(soup.find('h1', class_='text-center').text.split()[2:-2])
    file_name = normalize_to_filename(song_name)
    song_url = ('https://downloadmusicvk.ru' +
            soup.find('a', {'id':'download-audio'}).get('href'))
    
    try:
        download_file(folder + file_name, song_url)
    except ConnectionResetError:
        print('\t', file_name, 'not downloaded.')
    except ValueError:
        print('\t', file_name, 'not downloaded.')
    else:
        log_file.write_(log_url)

def download_file(file_path:str, url:str):
    with open(file_path, 'wb') as out:
        obj = requests.get(url, stream=True)
        for chunk in obj.iter_content(1024):
            out.write(chunk)

def normalize_to_filename(string:str)->str:
    for char in '\\/:*?"<>|':
        string = string.replace(char, ' ')
    return string + '.mp3'
