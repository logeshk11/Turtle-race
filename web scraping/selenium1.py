from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path="/Users/shankar/PycharmProjects/chrome/chromedriver.exe"

driver=webdriver.Chrome(executable_path=path)
driver.get("https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B09VK5D8KW/ref=sr_1_19?crid=28DZU1CU445WJ&keywords=samsung%2Bmobile%2Bphone&qid=1680762839&s=electronics&sprefix=samsung%2Bmi%2Celectronics%2C214&sr=1-19&th=1")

#price= driver.find_element(by=By.CLASS_NAME, value="a-price-whole")

# ps=driver.find_element(by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# print(ps.text)
# #print(price.tag_name)

action = driver.find_element(by=By.NAME, value="field-keywords")
action.send_keys("puma")
action.send_keys(Keys.ENTER)