# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:59:06 2019

@author: Rana Rajput
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser
import time
import constants

class BrowserBase(object):
    
    def __init__(self):
        self._browser = Browser.getInstance()
        self._delay = constants.DELAY
    
    # Get Element From XPath after when the element is present
    def get_element_from_xpath(self, xpath, wait=constants.DONT_WAIT):
        if wait == constants.WAIT_FOR_PRESENCE:
                WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        elif wait == constants.WAIT_FOR_CLICKABLE:
                WebDriverWait(self._browser, self._delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elif wait == constants.WAIT_FOR_PRESENCE_AND_CLICKABLE:
                WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
                WebDriverWait(self._browser, self._delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        time.sleep(1)
        element = self._browser.find_element_by_xpath(xpath)
        return element
        
    def quit(self):
        self.log("\tQuitting Browser")
        self._browser.quit()