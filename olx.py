from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
pages  = set()
def getLinks(url):
    global pages
    try:
        html = urlopen(url)
    except HTTPError as e:
        return e
    try:
        bsobj = BeautifulSoup(html, "lxml")
        Links = bsobj.find("div", {"class":"maincategories"}).findAll("a", href=re.compile("^(/)*"))
    except AttributeError as e:
        return None
    return Links

Links = getLinks("https://www.olx.co.ke/")
if Links == None:
    print("Could not find Links")
else:
    for link in Links:
        # print(bsobj.find(class="block link category-name").findAll("span")[0])
        if 'href' in link.attrs:
            print(link.attrs['href'])
    # print(listing-card__description)

