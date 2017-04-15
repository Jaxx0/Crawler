from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html, "lxml")
        Links = bsobj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        return None
    return Links
Links = getLinks("/wiki/Kenya")
if Links == None:
    print("Could not get links")
else:
    for link in Links:
        print(link.attrs['href'])
        File = open("kenyan_links.txt", "a")
        File.writelines(link.attrs['href'] + "\n")
    while len(Links) > 0:
        newWikiLink = Links[random.randint(0, len(Links)-1)].attrs['href']
        print(newWikiLink)
        file = open("wikilinks.txt", "a")
        file.writelines(newWikiLink + "\n")
        Links = getLinks(newWikiLink)


