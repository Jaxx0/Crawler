##    PRINTS OUT ROWS IN A TABLE

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html, "lxml")
for child in bsobj.find("table", {"id":"giftList"}).children:
    print(child)

## PRINTS OUT ROWS OF PRODUCTS FROM THE PRODUCT TABLE (Except first title row)

for sibling in bsobj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
print(bsobj.find("img", {"src":"../img/gifts/img3.jpg"}).parent.previous_sibling.get_text())
