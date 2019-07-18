# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:48:41 2019

@author: Rana Rajput
"""
import constants
import XPATH
from BrowserBase import BrowserBase

class Assert(BrowserBase):
    
    def test_if_element_selected(self, row_no, col_no):
        xpath = (XPATH.PREACHER_LANGUAGE.replace(constants.DUMMY_ROW_NO, row_no).replace(constants.DUMMY_COLUMN_NO, col_no))     
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if not element.is_selected():
            assert False, "\tElement was not selected at row: " + row_no + " and column: " + col_no
        else: 
            print ("\tElement was selected at row: " + row_no + " and column: " + col_no)
    
    def test_element_value(self, row_no, col_no, expected_value, by="value"):
        xpath = (XPATH.PREACHER_LANGUAGE.replace(constants.DUMMY_ROW_NO, row_no).replace(constants.DUMMY_COLUMN_NO, col_no))
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if by == "text":
            actual_value = element.text
        else:
            actual_value = element.get_attribute("value")
        if not actual_value == expected_value:
            assert False, ("\tAt row: " + row_no + " and column: " + col_no + ", EXPECTED VALUE IS: " + expected_value + " HOWEVER ACTUAL VALUE IS: " + actual_value)
        else:
            print ("\tThe expected value and actual value matches at row: " + row_no + " and column: " + col_no + " :, value is: " + actual_value)

