from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&N=-1&isNodeId=1'

uClient = uReq(my_url)

# offload content to variable
page_html = uClient.read()
uClient.close()

uClient.close()

# HTML page parser
page_soup = soup(page_html, "html.parser")

#grabs each products
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
    #Grabs title for every graphics card
    brand = container.a.img['title']
    title_container = container.findAll("a", {"class": "item-title"})

    product_name = title_container[0].text.strip()

    print ("brand " + brand)
    print ("name " + title_container)



