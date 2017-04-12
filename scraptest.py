from urllib.request import urlopen
html = urlopen("http://www.trufece.org/")
print(html.read())
