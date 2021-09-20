
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox()
driver.get("https://www.python.org/search/?q=pycon&submit=")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
ab = elem.get_attribute("innerHTML")
ab
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)


#WebDriverWait(driver, 10)
#driver.implicitly_wait(10)
#print("Waiten is gebeurd")


testab = driver.find_element_by_tag_name("body")
eb = testab.get_attribute("innerHTML")

#deas = testab.find_elements_by_tag_name("ul")
deas = testab.find_elements_by_class_name("list-recent-events")
deas[0].get_attribute("innerHTML")

cd = deas[0].find_elements_by_tag_name("li")
cd
counter = 0
for a in cd:
    counter = counter + 1
    if counter < 3:
        print(a.get_attribute("innerHTML"))
        print("=============================")

#for elem in deas:
 #   print(elem.get_attribute("innerHTML"))
    #print(">> een a id deas:" + elem.get_attribute("innerHTML"))
    

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/results?search_query=python")
elem = driver.find_element_by_tag_name("body")
ab = elem.get_attribute("innerHTML")
ab