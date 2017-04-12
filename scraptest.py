from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/")
Bsobj = BeautifulSoup(html.read(), "lxml")
print(Bsobj)
