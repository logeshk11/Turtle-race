from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path="/Users/shankar/PycharmProjects/chrome/chromedriver.exe"
website="https://londonappbrewery.com/sendy/subscription?f=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.245599044.15037476.1680769846-414676352.1680676370"
driver=webdriver.Chrome(executable_path=path)
driver.get(website)


name = driver.find_element(by=By.NAME, value="name")
name.send_keys("Logesh")

mail = driver.find_element(by=By.NAME, value="email")
mail.send_keys("logeshlearningpy@gmail.com")


check = driver.find_element(by=By.NAME, value="gdpr")
check.click()





time.sleep()

driver.quit()