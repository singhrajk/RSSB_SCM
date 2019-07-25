# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:48:41 2019

@author: Rana Rajput
"""
import constants
from BrowserBase import BrowserBase

class Assert(BrowserBase):
    
    def test_values(self, expected_value, actual_value):
        if not actual_value == expected_value:
            assert False, ("EXPECTED VALUE IS: " + expected_value + " HOWEVER ACTUAL VALUE IS: " + actual_value)
        else:
            print ("\tThe expected value and actual value matches: " + actual_value)

    def test_element_value_xpath(self, xpath, expected_value, by="value"):
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if by == "text":
            self.test_values(expected_value, element.text)
        else:
            self.test_values(expected_value, element.get_attribute("value"))
            

    def test_dropdown_value_xpath(self, xpath, expected_value, by="value"):
        selectedItems = self.get_selected_from_dropdown(xpath)
        self.test_values(expected_value, selectedItems.first_selected_option.text)
    
    def test_if_element_selected(self, xpath):
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        if not element.is_selected():
            assert False, "\tElement was not selected"
        else: 
            print ("\tElement was selected")
    
    def test_element_value_xpath1(self, xpath, expected_value, by="value"):
        element = self.get_element_from_xpath(xpath, constants.WAIT_FOR_PRESENCE)
        print (element)
        print (element.text)        
        print (element.get_attribute("value"))
        print (element.getText())
        #self.test_values(expected_value, element.get_attribute("value"))
