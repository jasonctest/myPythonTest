"""
@author: Jason Chan

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import time

# Initialize firefox webdriver
def _driver_init():
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 3)

	return driver


def login(driver, username, password):

	username_username_input = driver.find_element_by_id("username")
	username_password_input = driver.find_element_by_id("password")

	username_username_input.send_keys(username)
	username_password_input.send_keys(password)

	time.sleep(1)

	login_btn = driver.find_element_by_xpath("//*[@id=\"login\"]/button")
	login_btn.click()

	time.sleep(2)
	
	

if __name__ == "__main__":
	
	weburl = "http://the-internet.herokuapp.com/login"
	driver = _driver_init()
	
	
	driver.get(weburl)	#open url in Firefox browser

	valid_username="tomsmith"
	valid_password="SuperSecretPassword!"
	
	login_success = "You logged into a secure area!"
	

	invalid_username="jasonc"
	invalid_password="1212312"
	
	login_fail = "Your username is invalid!"

	#test 01
	login(driver, valid_username, valid_password)
	time.sleep(2)
	success_elem = driver.find_element_by_id("flash")
	
	assert success_elem.text.find(login_success) != -1

	if login_success in success_elem.text:
		print "test 01 pass"
	else:
		print "test 01 failed"
	
	#test 02
	driver.get(weburl) 
	login(driver, invalid_username, invalid_password)
	time.sleep(2)
	fail_elem = driver.find_element_by_class_name("error")
	assert fail_elem.text.find(login_fail) != -1
	if login_fail in fail_elem.text:
 		print "test 02 pass"
	else:   
		print "test 02 failed"

	driver.quit()

	




