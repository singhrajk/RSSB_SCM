# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from Tab import Tab
from selenium.webdriver.common.keys import Keys
import constants
import XPATH

class Centre(Tab):
    
    def __init__(self, search_input=""):
        super(Centre, self).__init__()
        self.search_input = search_input
        self._tab = "centre"
        self._group = "2"
        self._list_no = "2"
    
    def query_search(self):
        self.search_query(self._tab, self._group, self._list_no, constants.CHOICE_1, self.search_input)    
        # Add assert statements using xpath
    
    def insert(self):
        super(Centre, self).insert(constants.CHOICE_1)
        self.send_inputs(self.search_input, XPATH.CENTRE_LOOKUP_FIELD, clear = "true")
        self.click_select_button(self._tab)
        self.tab(5).send_inputs("Remarks: Automation Testing", clear = "true")
        self.tab().send_inputs("Land", dropdown = "true")
        self.tab().send_inputs("Leased", dropdown = "true")
        self.tab().send_inputs(Keys.DOWN)
        self.tab().send_inputs("Test", clear = "true")
        self.press_button(constants.BUTTON_SAVE, self._tab)
        
    def search(self, choice_no):
        super(Centre, self).search(choice_no)
        self.send_inputs("Week 4", XPATH.SCREENFIELD_INPUT)
        self.click_element(XPATH.SCREEN_LINK_ROW1_COL6)       
        print ("\tTEST for BANGALORE CENTRE , WEEK 4 Schedule\n")       
        self._assert.test_element_value_xpath(XPATH.CENTRE_LOOKUP_FIELD, "Bangalore")
        self._assert.test_dropdown_value_xpath(XPATH.WEEK_LOOKUP_FIELD, "Week 4")
        self._assert.test_dropdown_value_xpath(XPATH.WEEKDAY_LOOKUP_FIELD, "Sunday")
        self._assert.test_element_value_xpath(XPATH.LANGUAGE_LOOKUP_FIELD, "Audio/Video")
        self._assert.test_element_value_xpath(XPATH.TIME,"09:30:00.000")
        self._assert.test_dropdown_value_xpath(XPATH.STATUS, "Active")
        self.click_element(XPATH.CLOSE_BUTTON)

    def update(self):
        pass
        # Update the centre details using reverse tab, also test using xpath asserts