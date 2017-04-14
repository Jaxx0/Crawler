from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.olx.co.ke/ad/samsung-galaxy-a520-gold-ID15QNYa.html")
bsobj = BeautifulSoup(html, "lxml")
namelist = bsobj.findAll("meta", {"name":"description"})
for name in namelist:
    print(name) 