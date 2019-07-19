# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:36:21 2019

@author: Rana Rajput
"""
import constants

## XPaths
LOGIN = '//*[@id="login-button"]'
LOGOUT = '//*[@id="wdf_root_div_id"]/div[1]/div/div[2]/div/div[2]/a[2]'
MENU_GROUP = '//*[@id="mnugrp_' + constants.DUMMY_GROUP_NO + '"]'
BUTTON = '//*[@id="btn'+ constants.DUMMY_BUTTON +'"]'
CLOSE_BUTTON = '//*[@id="cboxClose"]'
LOOKUP_FIELD = '//*[@id="'+ constants.DUMMY_LOOKUP +'_Id_lookup"]'
ID_FIELD = '//*[@id="' + constants.DUMMY_ID + '"]'
GROUP_CHOICE = '//*[@id="wdf_root_div_id"]/div[1]/div/div[1]/ul/li[' + constants.DUMMY_LIST_NO + ']/ul/li[' + constants.DUMMY_CHOICE_NO + ']/span/span[1]'
EXPORT = '//*[@id="wdf-list-view row-fluid"]/div/div[1]/div/button'
SELECT = '//*[@id="divOptions"]/button'
SEARCH = '//*[@id="wdfScreenFieldSet"]/div/div/form/div[1]/fieldset/button'
CONFIRM = '/html/body/div[4]/div/div/div[2]/button[2]'
SCREENFIELDSET ='//*[@id="wdfScreenFieldSet"]/div/div/form/div[2]/div[2]/fieldset/div'
SCREENFIELD_INPUT = SCREENFIELDSET + '/div/div/input'
SCREENFIELD_TABLE_INPUT = SCREENFIELDSET + '/table/tbody/tr[' + constants.DUMMY_ROW_NO + ']/td[' + constants.DUMMY_COLUMN_NO + ']/input'
SCREENFIELD_TABLE_HREF =  SCREENFIELDSET + '/div/table/tbody/tr[' + constants.DUMMY_ROW_NO + ']/td[' + constants.DUMMY_COLUMN_NO + ']/a'
TIME = '//*[@id="time"]'
STATUS = '//*[@id="status"]'

