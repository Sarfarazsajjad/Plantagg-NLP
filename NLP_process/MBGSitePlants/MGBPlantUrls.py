import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderListResults.aspx?letter=B")
driver.set_window_size(1440, 900)



elems = driver.find_elements_by_xpath("//div[@id='dnn_ctr4157_SearchResults_pnlList']//a[contains(@href,'')]")
for elem in elems:
    
    print(elem.get_attribute("href"))
    file_object = open('B.txt', 'a')
    file_object.write(elem.get_attribute("href") + "\n")
    file_object.close()
driver.close()
