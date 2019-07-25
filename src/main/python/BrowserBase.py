# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:59:06 2019

@author: Rana Rajput
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from browser import Browser
import time
import constants

# Class to Interact with Browser
class BrowserBase(object):
    
    # Initialising the browser instance
    def __init__(self):
        self._browser = Browser.getInstance()
        self._delay = constants.DELAY
    
    def get_element(self, xpath = "none", wait = constants.DONT_WAIT):
        if not xpath == "none":
            return self.get_element_from_xpath(xpath, wait)
        else: 
            return self._browser.switch_to.active_element
        
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
    
    # Get the selected items of dropdown from xpath
    def get_selected_from_dropdown(self, xpath = "none", wait=constants.DONT_WAIT):
        return Select(self.get_element(xpath, wait))
    
    # Return true/false based on the element at xpath is active or not
    def is_element_active(self, xpath):
        return self.get_element(xpath) == self.get_element()
    
    def tab(self, number_of_times = 1, reverse = "false"):
        i = 0
        while i < number_of_times:
            if reverse == "false":
                self.get_element().send_keys(Keys.TAB)
            else:
                self.get_element().send_keys(Keys.LEFT_SHIFT + Keys.TAB)
            i = i + 1    # update counter   
        return self
        
    def quit(self):
        self.log("\tQuitting Browser")
        self._browser.quit()