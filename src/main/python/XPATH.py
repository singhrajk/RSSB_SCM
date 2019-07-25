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
ID_FIELD = '//*[@id="' + constants.DUMMY_ID + '"]'
GROUP_CHOICE = '//*[@id="wdf_root_div_id"]/div[1]/div/div[1]/ul/li[' + constants.DUMMY_LIST_NO + ']/ul/li[' + constants.DUMMY_CHOICE_NO + ']/span/span[1]'
EXPORT = '//*[@id="wdf-list-view row-fluid"]/div/div[1]/div/button'
SELECT = '//*[@id="divOptions"]/button'
SEARCH = '//*[@id="wdfScreenFieldSet"]/div/div/form/div[1]/fieldset/button'
CONFIRM = '/html/body/div[4]/div/div/div[2]/button[2]'
TIME = '//*[@id="time"]'
STATUS = '//*[@id="status"]'
MESSAGE_BAR = '"//*[@id="wdf_root_div_id"]/div[4]"'

## LOOKUP FIELDS
LOOKUP_FIELD = '//*[@id="'+ constants.DUMMY_LOOKUP +'_Id_lookup"]'
CENTRE_LOOKUP_FIELD = '//*[@id="'+ constants.CENTRE +'_Id_lookup"]'
LANGUAGE_LOOKUP_FIELD  = '//*[@id="'+ constants.LANGUAGE +'_Id_lookup"]'
WEEK_LOOKUP_FIELD  = '//*[@id="week_Id_lookup"]'
WEEKDAY_LOOKUP_FIELD  = '//*[@id="weekday_Id_lookup"]'
SECRETARY_LOOKUP_FIELD = '//*[@id="secretary_Id_lookup"]'
ALTERNATE_SEWADAR_LOOKUP_FIELD = '//*[@id="alternate_sewadar_Id_lookup"]'
FILE_NO_LOOKUP_FIELD = '//*[@id="file_no"]'
DUTY_ALLOCATION_AREA_LOOKUP_FIELD = '//*[@id="duty_allocation_area_Id_lookup"]'
REMARKS_LOOKUP_FIELD = '//*[@id="remarks"]'
LAND_TYPE_LOOKUP_FIELD = '//*[@id="landDetails_land_type_Id_lookup"]'
OWNERSHIP_TYPE_LOOKUP_FIELD = '//*[@id="landDetails_ownership_type_Id_lookup"]'
NATURE_OF_LAND_LOOKUP_FIELD = '//*[@id="landDetails_nature_of_land_Id_lookup"]'
LAND_EXTENT_LOOKUP_FIELD = '//*[@id="landDetails_land_extent"]'
LONGITUDE_LOOKUP_FIELD = '//*[@id="landDetails_longitude"]'
LATITUDE_LOOKUP_FIELD = '//*[@id="landDetails_latitude"]'
CURRENT_DOCUMENT_LOOKUP_FIELD = '//*[@id="currentDocument_document_type_Id_lookup"]'

## SCREENFIELDS
SCREENFIELDSET ='//*[@id="wdfScreenFieldSet"]/div/div/form/div[2]/div[2]/fieldset/div'
SCREENFIELD_INPUT = SCREENFIELDSET + '/div/div/input'
SCREENFIELD_TABLE_INPUT = SCREENFIELDSET + '/table/tbody/tr[' + constants.DUMMY_ROW_NO + ']/td[' + constants.DUMMY_COLUMN_NO + ']/input'
SCREENFIELD_TABLE_HREF =  SCREENFIELDSET + '/div/table/tbody/tr[' + constants.DUMMY_ROW_NO + ']/td[' + constants.DUMMY_COLUMN_NO + ']/a'
SCREEN_LINK_ROW1_COL1 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[1]/a'
SCREEN_LINK_ROW1_COL2 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[2]/a'
SCREEN_LINK_ROW1_COL3 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[3]/a'
SCREEN_LINK_ROW1_COL4 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[4]/a'
SCREEN_LINK_ROW1_COL5 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[5]/a'
SCREEN_LINK_ROW1_COL6 = SCREENFIELDSET + '/div/table/tbody/tr[1]/td[6]/a'
SCREEN_INPUT_ROW1_COL1 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[1]/input'
SCREEN_INPUT_ROW1_COL2 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[2]/input'
SCREEN_INPUT_ROW1_COL3 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[3]/input'
SCREEN_INPUT_ROW1_COL4 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[4]/input'
SCREEN_INPUT_ROW1_COL5 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[5]/input'
SCREEN_INPUT_ROW1_COL6 =  SCREENFIELDSET + '/table/tbody/tr[1]/td[6]/input'
SCREEN_INPUT_ROW2_COL1 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[1]/input'
SCREEN_INPUT_ROW2_COL2 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[2]/input'
SCREEN_INPUT_ROW2_COL3 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[3]/input'
SCREEN_INPUT_ROW2_COL4 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[4]/input'
SCREEN_INPUT_ROW2_COL5 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[5]/input'
SCREEN_INPUT_ROW2_COL6 =  SCREENFIELDSET + '/table/tbody/tr[2]/td[6]/input'


SCREENFIELDSET_CENTRE_AD = '//*[@id="wdfScreenFieldSet"]/div/div/form/div/div/fieldset[3]/div'
SCREENFIELDSET_CENTRE_AD_ROW1_COL1 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[1]/td[1]'
SCREENFIELDSET_CENTRE_AD_ROW1_COL2 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[1]/td[2]'
SCREENFIELDSET_CENTRE_AD_ROW1_COL3 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[1]/td[3]'
SCREENFIELDSET_CENTRE_AD_ROW1_COL4 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[1]/td[4]'
SCREENFIELDSET_CENTRE_AD_ROW2_COL1 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[2]/td[1]'
SCREENFIELDSET_CENTRE_AD_ROW2_COL2 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[2]/td[2]'
SCREENFIELDSET_CENTRE_AD_ROW2_COL3 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[2]/td[3]'
SCREENFIELDSET_CENTRE_AD_ROW2_COL4 =  SCREENFIELDSET_CENTRE_AD + '/table/tbody/tr[2]/td[4]'