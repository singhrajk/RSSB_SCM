# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:11:49 2019

@author: Niharika Jaidka
"""
from Browser import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import constants

class Tab:
    
    def __init__(self, browser):
        self._browser = browser
        
     # Load a particular page in the browser
    def load_page_in_browser(self, url, errorMsg):
        try:
            self._browser.get(url)
        except:
            self.log(errorMsg)

    # Get Element From XPath after when the element is present
    def get_element_from_xpath(self, xpath, wait):
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

    # Sends Input keys at a particular input on x path after it is present
    def send_inputs_at_xpath(self, xpath, keys, errorMsg):
        try:
            element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
            element.clear()
            element.send_keys(keys)
        except:
            self.log(errorMsg)

    # Click the element available at the X Path after it is Present & Clickable
    def click_element_at_xpath(self, xpath, errorMsg):
        try:
            element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
            element.click()
        except:
            self.log(errorMsg)

    # Select group on the screen
    def select_group(self, group_no, tab):
        self.click_element_at_xpath(constants.XPATH_MENU_GROUP.replace(constants.DUMMY_GROUP_NO, group_no), constants.ERROR_CLICK.replace(constants.DUMMY_TAB,tab))
    
    # Method to save the records by pressing SaveButton
    def press_button(self, btn, tab):
       self.click_element_at_xpath(constants.XPATH_BUTTON.replace(constants.DUMMY_BUTTON, btn),"Error while " + btn + " records for: " + tab + " tab")
    
    def send_keys_lookup(self, lookup_field, keys):
        self.send_inputs_at_xpath(constants.XPATH_LOOKUP_FIELD.replace(constants.DUMMY_LOOKUP, lookup_field), keys, "Error while sending keys: " + keys + " in field: " + lookup_field)
    
    def send_keys_id(self, id_field, keys):
        self.send_inputs_at_xpath(constants.XPATH_ID_FIELD.replace(constants.DUMMY_ID, id_field), keys, "Error while sending keys: " + keys + " in field: " + id_field)
     
    # Select the element in the list, Put the list_no as the position of the tab, put the choice_no as the position of the element
    def select_group_choice(self, list_no, choice_no):
        self.click_element_at_xpath((constants.XPATH_GROUP_CHOICE.replace(constants.DUMMY_LIST_NO, list_no)).replace(constants.DUMMY_CHOICE_NO, choice_no), "Error while clicking Centre Choice")

    def select_group_and_group_choice(self, tab, group_no, list_no, choice_no):
        self.select_group(group_no , tab)
        self.select_group_choice(list_no, choice_no)

    def click_select_button (self, tab):
        self.click_element_at_xpath(constants.XPATH_SELECT, constants.ERROR_SELECT.replace(constants.DUMMY_TAB,tab))

    def click_search_button (self, tab):
        self.click_element_at_xpath(constants.XPATH_SEARCH ,"Error while clicking search button: " + tab + " tab")

    # This method is to login on page, username , password will come from environment
    def login_on_page(self, url, username, password):
        try:
            self.log("\n\tPerforming login on the browser")
            self.load_page_in_browser(url, "Error Loading the page")
            self.send_keys_id(constants.FIELD_LOGIN, username)
            self.send_keys_id(constants.FIELD_PASSWORD, password)
            self.click_element_at_xpath(constants.XPATH_LOGIN, "Login Submit Error")
        except Exception as ex:
            self.log("Exception occurred in login: " + ex)
        
    # Method to test the export
    def test_export(self, tab, group_no, list_no, choice_no):
        self.log("\tPerforming export of the records for tab: " + tab)
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.press_button(constants.BUTTON_QUERY, tab)
        self.press_button(constants.BUTTON_GET, tab)
        self.click_element_at_xpath(constants.XPATH_EXPORT, constants.ERROR_EXPORT.replace(constants.DUMMY_TAB,tab))
    
    # Method to search something in a left hand tab
    def test_search(self, tab, group_no, list_no, choice_no, search_input):
        self.log("\tPerforming the search with input: " + search_input + " on the search/select menu for tab: " + tab)
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.send_keys_lookup(tab, search_input)
        time.sleep(1)
        self.click_select_button(tab)
        self.click_search_button(tab)
    
    # Method to 
    def test_search_query(self, tab, group_no, list_no, choice_no, search_input):
        self.log("\tPerforming the search with input: " + search_input + " on the query/search/select menu for tab: " + tab)
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.press_button(constants.BUTTON_QUERY, tab)
        self.send_keys_lookup(tab, search_input)
        self.click_select_button(tab)
        self.press_button(constants.BUTTON_GET, tab)
    
    def test_insert(self, tab, group_no, list_no, choice_no, input_details):
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        browser = self
        print (type(input_details))
        input_details.insert(tab, group_no, list_no, choice_no, browser)
        
    def test_delete(self, tab, group_no, list_no, choice_no, search_input):
        self.test_search_query(tab, group_no, list_no, choice_no, search_input)
        self.press_button(constants.BUTTON_DELETE, tab)
        self.click_element_at_xpath(constants.XPATH_CONFIRM,"Error while confirming in " + tab + " tab")        

    # Method to logout from the browser
    def logout(self):
        self.log("\tPerforming Logout")
        self.click_element_at_xpath(constants.XPATH_LOGOUT, "Logout Error")
    
    def log(self, input):
        print (input)