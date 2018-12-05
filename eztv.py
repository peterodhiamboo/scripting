import requests as req
from bs4 import BeautifulSoup as Soup

my_url = 'https://eztv.io/search/the-originals'

my_html = Soup(req.get(my_url).text, 'html.parser')

body = my_html.body

content_table = body.find_all('table', class_='forum_header_border')[2]

table_row = content_table.find_all('tr')


for trow in table_row:

    tdata = trow.find_all('td', class_='forum_thread_post')

    for tdat in tdata:
        episode_title = tdata[1].a.text
        magnet_link = tdata[2].find_all('a')[0]['href']
        download_torrent = tdata[2].find_all('a')[1]['href']

        file_size = tdata[3].text
        time_posted = tdata[4].text
        seeders = tdata[5].text

        
        print('NAME: ' + episode_title)
        print('MAGNET-LINK: '+ magnet_link)
        print('TORRENT-URL: ' + download_torrent)
        print('SIZE: ' + file_size)
        print('DURATION:' + time_posted)
        print('SEEDERS:' + seeders)
        print('------------------------------------------------------------')

# td = table_row.find_all('td', class_='forum_thread_post')

# for te in td:
#     print(te)
#     print('***************************************************************************')




# for all_rows in table_row:

#     for indi in all_rows.find_all('td'):
#         print(indi)
#     print('***************************************************************************')
