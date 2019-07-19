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
        xpath = (XPATH.SCREENFIELD_TABLE_INPUT.replace(constants.DUMMY_ROW_NO, row_no).replace(constants.DUMMY_COLUMN_NO, col_no))     
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if not element.is_selected():
            assert False, "\tElement was not selected at row: " + row_no + " and column: " + col_no
        else: 
            print ("\tElement was selected at row: " + row_no + " and column: " + col_no)
    
    def test_element_value_xpath(self, xpath, expected_value, by="value"):
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        actual_value = element.get_attribute("value")
        if not actual_value == expected_value:
            assert False, ("EXPECTED VALUE IS: " + expected_value + " HOWEVER ACTUAL VALUE IS: " + actual_value)
        else:
            print ("\tThe expected value and actual value matches: " + actual_value)
    
    def test_element_value_screenfield(self, row_no, col_no, expected_value, by="value"):
        xpath = (XPATH.SCREENFIELD_TABLE_INPUT.replace(constants.DUMMY_ROW_NO, row_no).replace(constants.DUMMY_COLUMN_NO, col_no))
        print ("\tChecking expected and actual values at row: " + row_no + " and column: " + col_no)
        self.test_element_value_xpath(xpath, expected_value, by)

    def test_element_value_lookup(self, lookup_id, expected_value, by="value"):
        self.test_element_value_xpath(XPATH.LOOKUP_FIELD.replace(constants.DUMMY_LOOKUP, lookup_id), expected_value)
