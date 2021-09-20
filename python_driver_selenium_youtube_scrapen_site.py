import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'http://youtube.com'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
website = soup.prettify()

driver = webdriver.Firefox()
driver.get("http://www.youtube.com")

#elem = driver.find_element_by_name("q")
heading1 = driver.find_element_by_tag_name('h1')

print(heading1.get_attribute("innerHTML"))

print("==================================")


URL = "https://mikrocentrum.nl/nl/high-tech-platform/leden/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
tabel = soup.find_all(class_="mb-3")
#rijen = soup.find_all('h3')

class Lid():
    bedrijfsnaam = 'onbekend'
    plaats = 'onbekende plaats'

leden = []

#print(tabel)

for elems in range (20):
    lid = Lid()
  #  titel = rijen[elems].find_all('p')
#    lid.bedrijfsnaam = tabel[elems].find_all(class_="font-weight-semibold")
    h = tabel[elems].find(class_="font-weight-semibold oi-content")
    if elems % 2 == 0:
        print(h.text)
        lid.bedrijfsnaam = h.text
 #   plaats = soup[elems].find_all (class_="item7-card-desc d-flex mt-1")
 #   lid.plaats = plaats[1].text
 #
        leden.append(lid)

#print(leden)
for l in leden:
    print (l.bedrijfsnaam)
    print (l.plaats)
