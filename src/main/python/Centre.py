# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019

@author: Rana Rajput
"""
from selenium.webdriver.common.keys import Keys
from Tab import Tab
#from browser import Browser
import constants

TAB_CENTRE = "centre"
GROUP_NO_CENTRE = "2"
LIST_NO_CENTRE = "2"
class Centre(Tab):
    
    def __init__(self, search_input):
        super(Centre, self).__init__()
        self.search_input = search_input

    def search_centre_schedule(self):
        self.test_search(TAB_CENTRE, GROUP_NO_CENTRE, LIST_NO_CENTRE, constants.CHOICE_2, self.search_input)
        
    def insert_centre_details(self):
        self.select_group_and_group_choice(TAB_CENTRE, GROUP_NO_CENTRE, LIST_NO_CENTRE, constants.CHOICE_1)
        self.log("\tPerforming the insert with input: " + self.search_input + " on the tab: " + TAB_CENTRE)
        self.send_keys_lookup(TAB_CENTRE, self.search_input)
        self.click_select_button(TAB_CENTRE)
        self.send_keys_lookup(constants.LAND_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.OWNERSHIP_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.LAND_NATURE, Keys.DOWN)
        self.send_keys_id(constants.LAND_EXTENT, constants.TEST)
        self.press_button(constants.BUTTON_SAVE, TAB_CENTRE)