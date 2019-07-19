# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:11:49 2019

@author: Rana Rajput
"""
from BrowserBase import BrowserBase
from AssertBase import Assert
import constants
import XPATH

class Tab(BrowserBase):

    def __init__(self):
        super(Tab, self).__init__()
        self._assert = Assert()
    
     # Load a particular page in the browser
    def load_page_in_browser(self, url, errorMsg):
        try:  
            self._browser.get(url)
        except Exception as ex:
            self.log(str(ex.message) + errorMsg)

    # Sends Input keys at a particular input on x path after it is present
    def send_inputs_at_xpath(self, xpath, keys, errorMsg="key could not be pressed"):
        try:
            element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
            #element.clear()
            element.send_keys(keys)
        except Exception as ex:
            self.log(str(ex.message) + errorMsg)

    # Click the element available at the X Path after it is Present & Clickable
    def click_element_at_xpath(self, xpath, errorMsg="Failed to click the button"):
        try:
            element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE_AND_CLICKABLE)
            element.click()
        except Exception as ex:
            self.log(str(ex.message) + errorMsg)

    # Select group on the screen
    def select_group(self, group_no, tab):
        self.click_element_at_xpath(XPATH.MENU_GROUP.replace(constants.DUMMY_GROUP_NO, group_no), constants.ERROR_CLICK.replace(constants.DUMMY_TAB,tab))
    
    # Method to save the records by pressing SaveButton
    def press_button(self, btn, tab):
       self.click_element_at_xpath(XPATH.BUTTON.replace(constants.DUMMY_BUTTON, btn),"Error while " + btn + " records for: " + tab + " tab")
    
    def send_keys_lookup(self, lookup_field, keys):
        self.send_inputs_at_xpath(XPATH.LOOKUP_FIELD.replace(constants.DUMMY_LOOKUP, lookup_field), keys, "Error while sending keys: " + keys + " in field: " + lookup_field)
    
    def send_keys_id(self, id_field, keys):
        self.send_inputs_at_xpath(XPATH.ID_FIELD.replace(constants.DUMMY_ID, id_field), keys, "Error while sending keys: " + keys + " in field: " + id_field)
     
    # Select the element in the list, Put the list_no as the position of the tab, put the choice_no as the position of the element
    def select_group_choice(self, list_no, choice_no):
        self.click_element_at_xpath((XPATH.GROUP_CHOICE.replace(constants.DUMMY_LIST_NO, list_no)).replace(constants.DUMMY_CHOICE_NO, choice_no), "Error while clicking Centre Choice")

    def select_group_and_group_choice(self, tab, group_no, list_no, choice_no):
        self.select_group(group_no , tab)
        self.select_group_choice(list_no, choice_no)

    def click_select_button (self, tab):
        self.click_element_at_xpath(XPATH.SELECT, constants.ERROR_SELECT.replace(constants.DUMMY_TAB,tab))

    def click_search_button (self, tab):
        self.click_element_at_xpath(XPATH.SEARCH ,"Error while clicking search button: " + tab + " tab")

    # This method is to login on page, username , password will come from environment
    def login_on_page(self, url, username, password):
        try:
            self.log("\n\tPerforming login on the browser")
            self.load_page_in_browser(url, "Error Loading the page")
            self.send_keys_id(constants.FIELD_LOGIN, username)
            self.send_keys_id(constants.FIELD_PASSWORD, password)
            self.click_element_at_xpath(XPATH.LOGIN, "Login Submit Error")
        except Exception as ex:
            self.log("Exception occurred in login: " + str(ex.message))
        
    # Method to test the export
    def export(self, choice_no):
        self.log("\tPerforming export of the records for tab: " + self._tab)
        self.select_group_and_group_choice(self._tab, self._group, self._list_no, choice_no)
        self.press_button(constants.BUTTON_QUERY, self._tab)
        self.press_button(constants.BUTTON_GET, self._tab)
        self.click_element_at_xpath(XPATH.EXPORT, constants.ERROR_EXPORT.replace(constants.DUMMY_TAB, self._tab))
    
    # Method to search something in a left hand tab
    def search(self, choice_no):
        self.log("\tPerforming the search with input: " + self.search_input + " on the search/select menu for tab: " + self._tab)
        self.select_group_and_group_choice(self._tab, self._group, self._list_no, choice_no)
        self.send_keys_lookup(self._tab, self.search_input)
        self.click_select_button(self._tab)
        self.click_search_button(self._tab)
    
    # Method to 
    def search_query(self, tab, group_no, list_no, choice_no, search_input):
        self.log("\tPerforming the search with input: " + search_input + " on the query/search/select menu for tab: " + tab)
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.press_button(constants.BUTTON_QUERY, tab)
        self.send_keys_lookup(tab, search_input)
        self.click_select_button(tab)
        self.press_button(constants.BUTTON_GET, tab)
        
    def delete(self, choice_no):
        self.search_query(self._tab, self._group, self._list_no, choice_no, self.search_input)
        self.press_button(constants.BUTTON_DELETE, self._tab)
        self.click_element_at_xpath(XPATH.CONFIRM,"Error while confirming in " + self._tab + " tab")        

    # Method to logout from the browser
    def logout(self):
        self.log("\tPerforming Logout")
        self.click_element_at_xpath(XPATH.LOGOUT, "Logout Error")
    
    def log(self, input):
        print (input)
    
       