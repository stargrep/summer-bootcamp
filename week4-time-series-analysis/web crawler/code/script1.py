from bs4 import BeautifulSoup

import requests
r = requests.get('http://en.wikipedia.org/wiki/Python_(programming_language)')
print(r.url)

soup = BeautifulSoup(r.text)
print(soup.find_all('a')[1:10])
