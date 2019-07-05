import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
from browser import Browser
import constants
import time

class FiddleTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """Start web browser"""
        delay = 60
        command_executor = os.getenv(constants.EXECUTOR,"")
        self._browser = Browser(command_executor, delay)
        try:
            username = os.getenv(constants.USERNAME,"")
            password = os.getenv(constants.PASSWORD,"")
            self._browser.login_on_page(constants.DERA_SCM_URL, username, password)
        except Exception as ex:
            self.fail(ex)

    def setUp(self):
        time.sleep(2)
        print (constants.STARS_START_LINE)
        print (constants.TEST_START  + self._testMethodName)

    # Do Nothing
    def test_0(self):
        pass

    # This will test search the centre schedule
    def test_1_search_centre_scehdule(self):
        try:
            self._browser.test_search(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, "2", "ba")
        except Exception as ex:
            self.fail(ex)

    def test_2_search_centre_details(self):
        try:
            self._browser.test_search_query(constants.TAB_CENTRE, constants.GROUP_NO_CENTRE, constants.LIST_NO_CENTRE, "1", "bangalore")
        except Exception as ex:
            self.fail(ex)

    # This will test export the centers
    def test_3_export_center(self):
        try:
            self._browser.test_export(constants.TAB_CENTRE , constants.GROUP_NO_CENTRE , constants.LIST_NO_CENTRE, "1")
        except Exception as ex:
            self.fail(ex)

    def test_4_search_preacher(self):
        try:
            self._browser.test_search_query(constants.LOOKUP_SEWADAR, constants.GROUP_NO_PREACHER, constants.LIST_NO_PREACHER, "1", "GUL")
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    def test_5_export_preacher(self):
        try:
            self._browser.test_export(constants.TAB_PREACHER , constants.GROUP_NO_PREACHER , constants.LIST_NO_PREACHER, "1")
        except Exception as ex:
            self.fail(ex)
    
    def tearDown(self):
        print (constants.TEST_FINSIH  + self._testMethodName)
        if sys.exc_info() == (None, None, None):
            print (constants.TEST_PASS)
        else:
            print (constants.TEST_FAIL)
        print (constants.STARS_END_LINE)
        
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

if __name__ == '__main__':
    unittest.main()