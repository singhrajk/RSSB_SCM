# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:23 2019
"""
import constants
from selenium.webdriver.common.keys import Keys
from Tab import Tab

class Centre(Tab):

    def __init__(self, search_input, browser):
        super(Centre, self).__init__(browser)
        self.search_input = search_input

    @property
    def search_input(self):
        return self.search_input

    @search_input.setter
    def age(self, value):
        self.search_input = value
       
    def insert(self, tab, group_no, list_no, choice_no):
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.log("\tPerforming the insert with input: " + self.search_input() + " on the tab: " + tab)
        self.send_keys_lookup(tab, self.search_input())
        self.click_select_button(tab)
        self.send_keys_lookup(constants.LAND_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.OWNERSHIP_TYPE, Keys.DOWN)
        self.send_keys_lookup(constants.LAND_NATURE, Keys.DOWN)
        self.send_keys_id(constants.LAND_EXTENT, constants.TEST)
        self.press_button(constants.BUTTON_SAVE, tab)