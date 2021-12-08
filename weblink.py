from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/StaticAnalyzer/?name=app-debug.apk&type=apk&checksum=5ee4829065640f9c936ac861d1650ffc")
elem1 = driver.find_elements_by_link_text("Start Dynamic Analysis")
elem1.click()
