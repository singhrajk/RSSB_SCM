# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:32:49 2019

@author: Rana Rajput
"""
from Tab import Tab
import constants
import XPATH

class Preacher(Tab):

    def __init__(self, search_input=""):
        super(Preacher, self).__init__()
        self.search_input = search_input
        self._tab = "preacher"
        self._group = "4"
        self._list_no = "3"

    def query_search(self):
        self.search_query(constants.LOOKUP_SEWADAR, self._group, self._list_no, constants.CHOICE_1, self.search_input)

    def insert(self):
        pass
    
    def search(self, choice_no):
       super(Preacher, self).search(choice_no)       
       ##ROW 1 GUL H MAKHIJA 
       self._assert.test_if_element_selected(XPATH.SCREEN_INPUT_ROW1_COL1)
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW1_COL3, "1672/ BANGALORE -C/KR/415")
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW1_COL4, "2003-01-13")
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW1_COL5, "Senior Sewadar")
       ## ROW 2 GUL H MAKHIJA 
       self._assert.test_if_element_selected(XPATH.SCREEN_INPUT_ROW2_COL1)
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW2_COL3, "1672/ BANGALORE -C/KR/415")
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW2_COL4, "2003-01-13")
       self._assert.test_element_value_xpath(XPATH.SCREEN_INPUT_ROW2_COL5, "Senior Sewadar")
   
