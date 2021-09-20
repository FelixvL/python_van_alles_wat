import requests
from bs4 import BeautifulSoup

URL = 'https://coinmarketcap.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
tabel = soup.find('tbody')
rijen = tabel.find_all('tr')

class Belegging:
    naam = 'onbekend'
    prijs = -1

beleggingen = []

for elems in range(10):
    belegging = Belegging()
    titel = rijen[elems].find_all('p')	
    belegging.naam = titel[1].text
    prijs = rijen[elems].find_all('a')
    belegging.prijs = prijs[1].text
    beleggingen.append(belegging)

#print(beleggingen)

for b in beleggingen:
    print(b.naam)
    print(b.prijs)