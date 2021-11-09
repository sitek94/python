from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.dr-chuck.com/page1.htm'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, features="html.parser")

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
