from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.proxy import *

myProxy = "host:8080"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

def main():

    for i in range(0,100):
        browser = webdriver.Firefox() # Get local session of firefox
        #driver = webdriver.Firefox(proxy=proxy)
        time.sleep(2.5)
        driver.get("http://www.winnbits.com") # Load page
        #elem = browser.find_element_by_id("adbit-displayed-ad-D97FC17D21") # Find the query box
        time.sleep(2.5) # Let the page load, will be added to the API
        #elem.click()
        driver.quit()

    if __name__ == '__main__':
        main()
