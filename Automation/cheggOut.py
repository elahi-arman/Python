#Arman Elahi -- Chegg Purchase Python Driver
#Sys and Selenium libraries are used extensively
#Usage requires the installation of Python and Selenium


import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def logIn(driver, username, passwd):
	email = driver.find_element_by_class_name('email-field')
	email.send_keys(username)
	password = driver.find_element_by_name('password')
	password.send_keys(passwd)
	submit = driver.find_element_by_name('login')
	submit.send_keys(Keys.RETURN)

def search(driver, book):
	search = driver.find_element_by_class_name('sihp-input-field')
	try:
		search.send_keys(book)
		search.send_keys(Keys.RETURN)
	except:
		print "Page Timeout"

#For these three methods, we take the time let it load before carrying on

def book_page(driver):
	driver.implicitly_wait(10) 
	try:
		next_page = driver.find_element_by_partial_link_text('Buy')
		next_page.click()
	except:
		print "Page Timeout"


def buy(driver, book):
	driver.implicitly_wait(10)
	try:
		next_page = driver.find_element_by_class_name('pricebox-add-to-cart')
		next_page.click()
	except:
		print "Page Timeout"

def quantity(driver):
	try:
		driver.implicitly_wait(10)
		quantity_box = driver.find_element_by_class_name('qty-box')
		quantity_box.send_keys(Keys.BACKSPACE)
		quantity_box.send_keys("2")
		submit = driver.find_element_by_class_name('btn-checkout')
		submit.click()
	except:
		print "Page Timeout"

#Begin the main driving program
def main():
	"""Usage: cheggOut.py [username] [password] [book]"""		#DOCSTRING

	if (len(sys.argv) < 3):
		print "Usage: cheggOut.py [username] [password] [book]"
		sys.exit()

	username = sys.argv[1]
	passwd = sys.argv[2]
	book = sys.argv[3]

	driver = webdriver.Firefox()
	driver.get("https://www.chegg.com/auth?action=login")
	logIn(driver, username, passwd)								#logging into chegg

	driver.forward()											#Searching for book
	search(driver, book)

	driver.forward()											#assume top result is correct
	book_page(driver)
	
	driver.forward()											#Adding book to cart
	buy(driver, book)

	driver.forward()											#changing quantity
	quantity(driver)

	driver.implicitly_wait(10)
	driver.quit()


if __name__ == '__main__':
	main()

