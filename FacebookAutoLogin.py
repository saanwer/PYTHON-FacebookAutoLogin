import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Facebook Auto Login
#Coded by | WarLord
#https://github.com/saanwer
def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("email", help="Facebook email")
	parser.add_argument("password", help="Facebook password")
	args = parser.parse_args()

	browser = webdriver.Firefox()
	browser.get("https://www.facebook.com/login.php")

	emailElement = browser.find_element_by_id("email")
	emailElement.send_keys(args.email)
	passElement = browser.find_element_by_id("pass")
	passElement.send_keys(args.password)
	passElement.submit()

	os.system('cls')#os.system('clear') if Linux
	print "[+] Auto login success!"
	browser.close()

if __name__ == "__main__":
	Main()
