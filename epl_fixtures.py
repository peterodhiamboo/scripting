import requests
from bs4 import BeautifulSoup as soup

my_url = 'http://13.127.45.89'
html = soup(requests.get(my_url).content, 'html.parser')


atags = html.find_all('a')


#13.126.14.151

for a in atags:
    #if(a.get('href').split('/')[0] == 'http:'):
        print(a.get('href'))


