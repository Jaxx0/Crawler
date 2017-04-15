from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
pages = set()
def getLinks(pageUrl):
    global pages
    try:
        html = urlopen("http://en.wikipedia.org" + pageUrl)
    except HTTPError as e:
        return e
    try:
        bsobj = BeautifulSoup(html, "lxml")
        Links = bsobj.findAll("a", href=re.compile("^(/wiki/)"))
        print(bsobj.h1.get_text())
        print(bsobj.find(id="mw-content-text").findAll("p")[0].get_text())
        print(bsobj.find(id="mw-content-text").findAll("p")[2].get_text())
    except IndexError as e:
        print("Something is missing from this page but don't you worry")
    return Links
Links = getLinks("/wiki/kenya")
if Links == None:
    print("Could not find the Page!")
else:
    for link in Links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-------------\n" +newPage)
                pages.add(newPage)
                getLinks(newPage)
                file = open("siteinfo.txt", "a")
                file.write(newPage +"\n")
getLinks("")