from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())

# Fetch internal links on a page
def getInternalinks(bsobj, includeUrl):
    internallinks = []
    inLinks = bsobj.findAll("a", href=re.compile("^(/|.|#*"+includeUrl+")"))
    for link in inLinks:
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks

# Fetch external links on a page
def getExternallinks(bsobj, excludeUrl):
    externallinks = []
    exlinks = bsobj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$"))
    for link in exlinks:
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "lxml")
    externallinks = getExternallinks(bsObj, splitAddress(startingPage)[0])
    if len(externallinks) == 0:
        internallinks = getInternallinks(bsObj, startingPage)
        return getNextExternallink(internallinks[random.randint(0,
            len(internallinks)-1)])
    else:
        return externallinks[random.randint(0, len(externallinks)-1)]
def followExternalOnly(startingSite):
    externallink = getRandomExternalLink("https://www.standardmedia.co.ke")
    print("Random external link is: "+externallink)
    file = open("random_links.txt", "a")
    file.writelines(externallink + "\n")
    followExternalOnly(externallink)
followExternalOnly("https://www.")

# #Collects a list of all external URLs found on the site
# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
#     try:
#          html = urlopen(siteUrl)
#     except HTTPError as e:
#         return e
#     except URLError as e:
#         return e
#     try:
#         bsObj = BeautifulSoup(html, "lxml")
#         internallinks = getInternalinks(bsObj, splitAddress(siteUrl)[0])
#         externallinks = getExternallinks(bsObj, splitAddress(siteUrl)[0])
#     except AttributeError as e:
#         return e
#     except ValueError as e:
#         return e
#     for link in externallinks:
#         if link not in allExtLinks:
#             allExtLinks.add(link)
#     for link in internallinks:
#         if link not in allIntLinks:
#             print(link)
#             allIntLinks.add(link)
#             getAllExternalLinks(link)
# getAllExternalLinks("http://www.google.com")


