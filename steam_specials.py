from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
 
 
 
my_url = 'https://store.steampowered.com/search/?specials=1&os=win'
uClient = urlopen(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
rows = containers = page_soup.findAll("a",{"class":"search_result_row"})


#Individual game title

for row in rows:
    game = row[0].findAll("span", {"class":"title"})
    game_title = game[0].text




