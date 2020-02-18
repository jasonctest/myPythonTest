"""
@author: Jason Chan

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


# Initialize firefox webdriver
def _driver_init():
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 3)

	return driver


if __name__ == "__main__":
	
	weburl = "http://the-internet.herokuapp.com/"
	driver = _driver_init()
	
	
	driver.get(weburl)	#open url in Firefox browser

	
	#Start writing test cases here ...
