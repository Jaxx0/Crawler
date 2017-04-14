from urllib import urlopen
from bs4 import BeautifulSoup
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsobj = BeautifulSoup(html.read(), "lxml")
        title = bsobj.body
    except AttributeError as e:
        return None

    return title

title = get_title("http://www.pythonscraping.com/pages/warandpeace.html")
if title == None:
    print("Could not find title")
else:
    print(title)

