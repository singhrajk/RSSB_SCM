"""
constants.py
"""

DELAY = 60

## UI Constants
TEST = "TEST"
DERA_SCM_URL = "https://derapps-staging.azurewebsites.net/SCM"

CHOICE_1 = "1"
CHOICE_2 = "2"

ROW_1 = "1"
ROW_2 = "2"

COLUMN_1 = "1"
COLUMN_2 = "2"
COLUMN_3 = "3"
COLUMN_4 = "4"
COLUMN_5 = "5"

LOOKUP_SEWADAR ="sewadar"
CENTRE = "centre"
LANGUAGE = "language"

LAND_TYPE = "landDetails_land_type"
OWNERSHIP_TYPE = "landDetails_ownership_type"
LAND_NATURE = "landDetails_nature_of_land"
LAND_EXTENT = "landDetails_land_extent"

## Dev Constants
WAIT_FOR_PRESENCE = 1
WAIT_FOR_CLICKABLE = 2
WAIT_FOR_PRESENCE_AND_CLICKABLE = 3
DONT_WAIT = 3
BUTTON_SAVE = "Save"
BUTTON_QUERY = "Query"
BUTTON_GET = "Get"
BUTTON_DELETE = "Delete"
BUTTON_INSERT = "Insert"
FIELD_LOGIN = "LoginId"
FIELD_PASSWORD = "Password"

## Dummies to be replaced
DUMMY_TAB = "$tab"
DUMMY_GROUP_NO = "$group_no"
DUMMY_CHOICE_NO = "$choice_no"
DUMMY_LIST_NO = "$list_no"
DUMMY_BUTTON = "$button"
DUMMY_LOOKUP = "$lookup"
DUMMY_ID = "$idfield"
DUMMY_ROW_NO = "$row_no"
DUMMY_COLUMN_NO = "$col_no"


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
