"""
constants.py
"""

DELAY = 60

## UI Constants
TEST = "TEST"
DERA_SCM_URL = "https://derapps-staging.azurewebsites.net/SCM"

TAB_CENTRE = "centre"
GROUP_NO_CENTRE = "2"
LIST_NO_CENTRE = "2"
CHOICE_1 = "1"
CHOICE_2 = "2"

TAB_PREACHER = "preacher"
GROUP_NO_PREACHER = "4"
LIST_NO_PREACHER = "3"

LOOKUP_SEWADAR ="sewadar"

LAND_TYPE = "landDetails_land_type"
OWNERSHIP_TYPE = "landDetails_ownership_type"
LAND_NATURE = "landDetails_nature_of_land"
LAND_EXTENT = "landDetails_land_extent"

## Dev Constants
WAIT_FOR_PRESENCE = 1
WAIT_FOR_CLICKABLE = 2
WAIT_FOR_PRESENCE_AND_CLICKABLE = 3
BUTTON_SAVE = "Save"
BUTTON_QUERY = "Query"
BUTTON_GET = "Get"
BUTTON_DELETE = "Delete"
BUTTON_INSERT = "Insert"
FIELD_LOGIN = "LoginId"
FIELD_PASSWORD = "Password"

## Dummies to be replaced
DUMMY_GROUP_NO = "$group_no"
DUMMY_CHOICE_NO = "$choice_no"
DUMMY_LIST_NO = "$list_no"
DUMMY_TAB = "$tab"
DUMMY_BUTTON = "$button"
DUMMY_LOOKUP = "$lookup"
DUMMY_ID = "$idfield"

## XPaths
XPATH_LOGIN = '//*[@id="login-button"]'
XPATH_LOGOUT = '//*[@id="wdf_root_div_id"]/div[1]/div/div[2]/div/div[2]/a[2]'
XPATH_MENU_GROUP = '//*[@id="mnugrp_' + DUMMY_GROUP_NO + '"]'
XPATH_BUTTON = '//*[@id="btn'+ DUMMY_BUTTON +'"]'
XPATH_LOOKUP_FIELD = '//*[@id="'+ DUMMY_LOOKUP +'_Id_lookup"]'
XPATH_ID_FIELD = '//*[@id="' + DUMMY_ID + '"]'
XPATH_GROUP_CHOICE = '//*[@id="wdf_root_div_id"]/div[1]/div/div[1]/ul/li[' + DUMMY_LIST_NO + ']/ul/li[' + DUMMY_CHOICE_NO + ']/span/span[1]'
XPATH_EXPORT = '//*[@id="wdf-list-view row-fluid"]/div/div[1]/div/button'
XPATH_SELECT = '//*[@id="divOptions"]/button'
XPATH_SEARCH = '//*[@id="wdfScreenFieldSet"]/div/div/form/div[1]/fieldset/button'
XPATH_CONFIRM = '/html/body/div[4]/div/div/div[2]/button[2]'

## Error Messages
ERROR_CLICK = "Error while clicking: " + DUMMY_TAB + " tab"
ERROR_EXPORT = "Error while exporting : " + DUMMY_TAB + " tab"
ERROR_SELECT = "Error while clicking select button: " + DUMMY_TAB + " tab"

## Browser or Site Specific Constants
EXECUTOR = "CMD_EXECUTOR"
USERNAME = "SITE_LOGIN_USER"
PASSWORD = "SITE_LOGIN_PWD"

## Console Constants
TEST_NUMBER_PATTERN = '^test_[0-9 ]*'
EMPTY = ''
NEW_LINE = "\n"
UNDERSCORE = "_"
SPACE = " "
STARS_LINE = "************************************************"
STARS_START_LINE = NEW_LINE + STARS_LINE
STARS_END_LINE = STARS_LINE + NEW_LINE
TEST_START = "Started Testing : "
TEST_FINSIH = "Finished Testing : "
TEST_PASS = "RESULT: PASSED"
TEST_FAIL = "RESULT: FAILED"
