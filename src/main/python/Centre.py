# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from selenium.webdriver.common.keys import Keys
from Tab import Tab
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
    
    def insert(self):
        self.select_group_and_group_choice(self._tab, self._group, self._list_no, constants.CHOICE_1)
        self.log("\tPerforming the insert with input: " + self.search_input + " on the tab: " + self._tab)
        self.send_keys_lookup(self._tab, self.search_input)
        self.click_select_button(self._tab)
        self.send_keys_lookup(constants.LAND_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.OWNERSHIP_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.LAND_NATURE, Keys.DOWN)
        self.send_keys_id(constants.LAND_EXTENT, constants.TEST)
        self.press_button(constants.BUTTON_SAVE, self._tab)
        
    def search(self, choice_no):
        super(Centre, self).search(choice_no)
        self.send_inputs_at_xpath(XPATH.SCREENFIELD_INPUT, "Week 4")
        self.click_element_at_xpath((XPATH.SCREENFIELD_TABLE_HREF.replace(constants.DUMMY_ROW_NO, "1").replace(constants.DUMMY_COLUMN_NO, "6")))       
        print ("\tTEST for BANGALORE CENTRE , WEEK 4 Schedule\n")       
        self._assert.test_element_value_lookup(constants.CENTRE, "Bangalore")
        #self._assert.test_element_value_lookup("week", "Week 4")
        #self._assert.test_element_value_lookup("weekday", "Sunday")  
        self._assert.test_element_value_lookup(constants.LANGUAGE, "Audio/Video")
        self._assert.test_element_value_xpath(XPATH.TIME,"09:30:00.000")
        #self._assert.test_element_value_xpath(XPATH.STATUS,"Active")
        self.click_element_at_xpath(XPATH.CLOSE_BUTTON)