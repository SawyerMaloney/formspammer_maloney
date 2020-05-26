from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--headless")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options=option, executable_path = PATH)
# driver = webdriver.PhantomJS(executable_path=PATH)

def func(x):
	time.sleep(.1)
	answer = ""
	driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfzomDlMbruxN7ztYjNrIfXURMeae3VEKfz1UtVyK2hIEqkZg/viewform")
	prove_not_robot = driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[1]/div/div/div')
	pnr_text = ""

	for value in prove_not_robot:

		pnr_text += value.text

	answer = pnr_text.split('"')[1]

	password_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')

	password_input.send_keys(answer)

	insta_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
	insta_input.send_keys('u mad cute homes' + str(x))
	print(str(x))

	submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
	submit.click()

for i in range(10):

	func(i)

	time.sleep(2)

print('finish')