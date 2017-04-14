from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def get_namelist(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html, "lxml")
        namelist = bsobj.find("table", {"class":"details fixed marginbott20 margintop5 full"})
    except AttributeError as e:
        return None
    return namelist

namelist = get_namelist("https://www.olx.co.ke/ad/toyota-landcruiser-prado-ID15QKk3.html#clm-ke_r2-2_id1002599911")
if namelist == None:
    print("Info could not be found")
else:
    for name in namelist:
        print(name)

