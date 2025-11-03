'''
Web scraping is I/O bound task, because we spend a lot of time waiting for responses from server
'''

# https://www.langchain.com/langchain
# https://academy.langchain.com/
# https://docs.langchain.com/?_gl=1*15aqfpf*_gcl_au*OTcyMTI2OTYwLjE3NjIxODY1ODk.*_ga*MTA0NjcyNjEyNS4xNzYyMTg2NTkw*_ga_47WX3HKKY2*czE3NjIxODY1ODkkbzEkZzAkdDE3NjIxODY1ODkkajYwJGwwJGgw

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.langchain.com/langchain',
    'https://academy.langchain.com/',
    'https://docs.langchain.com/?_gl=1*15aqfpf*_gcl_au*OTcyMTI2OTYwLjE3NjIxODY1ODk.*_ga*MTA0NjcyNjEyNS4xNzYyMTg2NTkw*_ga_47WX3HKKY2*czE3NjIxODY1ODkkbzEkZzAkdDE3NjIxODY1ODkkajYwJGwwJGgw'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetch {len(soup.text)} characters from {url}')
    # print(soup.text)


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("all web pages fetched")