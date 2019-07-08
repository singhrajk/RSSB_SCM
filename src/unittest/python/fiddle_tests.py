import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
from browser import Browser
import constants
import time
import re

class FiddleTest(unittest.TestCase):
    
    # Method getting the test name
    def getTestName(self):
        testMethodName = re.sub(constants.TEST_NUMBER_PATTERN, constants.EMPTY, self._testMethodName, 1)
        return testMethodName.replace(constants.UNDERSCORE, constants.SPACE)
    
    # setup method, called once before all the tests
    @classmethod
    def setUpClass(self):
        command_executor = os.getenv(constants.EXECUTOR,"")
        username = os.getenv(constants.USERNAME,"")
        password = os.getenv(constants.PASSWORD,"")
        """Start web browser"""
        self._browser = Browser(command_executor, constants.DELAY)
        self._browser.login_on_page(constants.DERA_SCM_URL, username, password)
    
    # setup method, called before each test
    def setUp(self):
        time.sleep(2)
        self._browser.log(constants.STARS_START_LINE)
        self._browser.log(constants.TEST_START  + self.getTestName())

    # Do Nothing
    def test_0_Nothing(self):
        pass

    # This will test search the centre schedule
    def test_1_Centre_Search_Schedule(self):
        try:
            self._browser.test_search(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_2, "ba")
        except Exception as ex:
            self.fail(ex)

    # This will search a particular centre details
    def test_2_Centre_Search_Centre_Details(self):
        try:
            self._browser.test_search_query(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1, "bangalore")
        except Exception as ex:
            self.fail(ex)
    
    # This will delete centre details
    def test_3_Centre_Delete_Centre_Details(self):
        try:
            self._browser.test_delete(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1, "Gawla")
        except Exception as ex:
            self.fail(ex)
    
    # This will insert centre details
    def test_4_Centre_Insert_Centre_Details(self):
        try:
            self._browser.test_centre_insert(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1, "Gawla")
        except Exception as ex:
            self.fail(ex)

    # This will test export the centers
    def test_5_Centre_Export_Centre_Details(self):
        try:
            self._browser.test_export(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will search a sewadar
    def test_6_Preacher_Search_Sewadar_Details(self):
        try:
            self._browser.test_search_query(constants.LOOKUP_SEWADAR, constants.GROUP_NO_PREACHER, constants.LIST_NO_PREACHER, constants.CHOICE_1, "GUL")
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    def test_7_Preacher_Export_Preacher_Details(self):
        try:
            self._browser.test_export(constants.TAB_PREACHER, constants.GROUP_NO_PREACHER, constants.LIST_NO_PREACHER, constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will run at end of each test
    def tearDown(self):
        self._browser.log(constants.TEST_FINSIH  + self.getTestName())
        self.logResult()
        self._browser.log(constants.STARS_END_LINE)
    
    # This will run at end of all tests 
    @classmethod
    def tearDownClass(self):
        """Logout browser"""
        try:
            time.sleep(2)
            self._browser.logout();
        except Exception as ex:
            self.fail(ex)
        time.sleep(4)
        self._browser = None
    
    # Method to log the result
    def logResult(self):
        if sys.exc_info() == (None, None, None):
            self._browser.log(constants.TEST_PASS)
        else:
            self._browser.log(constants.TEST_FAIL)

if __name__ == '__main__':
    unittest.main()