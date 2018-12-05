from bs4 import BeautifulSoup as soup
import requests
import lxml

my_url = 'http://www.espn.com/soccer/standings/_/league/eng.1'
raw_html = requests.get(my_url).text

formated_html = soup(raw_html, 'lxml')

premier_league = formated_html.find_all('tr', class_='standings-row')
# points = premier_league.find_all('td')

# print(points[8].text)



i = 1

for teams in premier_league :
    name = teams.find('span', class_='team-names').text
    points = teams.find_all('td')
    mapoints = points[8].text
    GD = points[7].text
    print("%d --> %s has %s points and %s GD" % (i, name, mapoints, GD))
    print()
    i = i+1
