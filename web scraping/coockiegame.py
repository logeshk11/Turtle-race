from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path="/Users/shankar/PycharmProjects/chrome/chromedriver.exe"
website="https://orteil.dashnet.org/cookieclicker/"

driver=webdriver.Chrome(executable_path=path)
driver.get(website)

driver.quit()












driver.quit()