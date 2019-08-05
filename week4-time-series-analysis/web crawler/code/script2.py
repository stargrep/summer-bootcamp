from bs4 import BeautifulSoup

import requests
r = requests.get('http://en.wikipedia.org/wiki/Python_(programming_language)')
print(r.url)

soup = BeautifulSoup(r.text)
links = []
for line in soup.find_all('a', href=True):
  links.append(line['href'])

print('\n'.join(links[1:10]))
print('\n'.join(links[-10:-1]))
