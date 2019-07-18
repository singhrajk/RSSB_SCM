# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from selenium.webdriver.common.keys import Keys
from Tab import Tab
import constants

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
       ##ROW 1 BANGALORE 
       #self._assert.test_element_value(constants.ROW_1, constants.COLUMN_2, "Week 1", "text")
       #self._assert.test_element_value(constants.ROW_1, constants.COLUMN_3, "Sunday", "text")
       #self._assert.test_element_value(constants.ROW_1, constants.COLUMN_4, "09:30:00", "text")
       #self._assert.test_element_value(constants.ROW_1, constants.COLUMN_5, "Hindi", "text")
       ## ROW 2 BANGALORE
       #self._assert.test_element_value(constants.ROW_2, constants.COLUMN_2, "Week 2", "text")
       #self._assert.test_element_value(constants.ROW_2, constants.COLUMN_3, "Sunday", "text")
       #self._assert.test_element_value(constants.ROW_2, constants.COLUMN_4, "09:30:00", "text")
       #self._assert.test_element_value(constants.ROW_2, constants.COLUMN_5, "English", "text")
   