from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None

	try:
		bsObj = BeautifulSoup(html.read(), "lxml")
		title = bsObj.h1
	except AttributeError as e:
		return None
		
	return title
	##########################################
	
	title = getTitle("http://www.reprapmall.com")
	if title == None:
		print("Could not find title")
	else:
		print(title)
