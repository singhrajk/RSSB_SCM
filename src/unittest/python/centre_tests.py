import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
import constants
import time
import re
from centre import Centre
from tab import Tab

class CentreTest(unittest.TestCase):

    # Method getting the test name
    def getTestName(self):
        test_name = re.sub(constants.TEST_NUMBER_PATTERN, constants.EMPTY, self._testMethodName, 1).title()
        test_name = self.__class__.__name__ + " : " + test_name.replace(constants.UNDERSCORE, constants.SPACE)
        return test_name

    # setup method, called once before all the tests
    @classmethod
    def setUpClass(self):
        username = os.getenv(constants.USERNAME,"")
        password = os.getenv(constants.PASSWORD,"")
        """Start web browser"""
        self._browser = Tab()
        self._browser.login_on_page(constants.DERA_SCM_URL, username, password)

    # setup method, called before each test
    def setUp(self):
        time.sleep(2)
        self._browser.log(constants.STARS_START_LINE)
        self._browser.log(constants.TEST_START  + self.getTestName())

    # This will test search the centre schedule
    def test_1_search_schedule(self):
        try:
            Centre().search_schedule("ba")
        except Exception as ex:
            self.fail(str(ex.message))

    # This will search a particular centre details
    def test_2_search_details(self):
        try:
            Centre().search_details("bangalore")
        except Exception as ex:
            self.fail(str(ex.message))

    # This will delete centre details
    def test_3_delete_details(self):
        try:
            Centre().delete_details("Gawla")
        except Exception as ex:
            self.fail(str(ex.message))

    # This will insert centre details
    def test_4_insert_details(self):
        try:
            Centre().insert_details("Gawla")
        except Exception as ex:
            self.fail(str(ex.message))

    # This will test export the centers
    def test_5_export_details(self):
        try:
            Centre().export_details()
        except Exception as ex:
            self.fail(str(ex.message))

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
            raise Exception("Tear Down Failed : {}.".format(ex))
        time.sleep(4)
        self._browser.quit()

    # Method to log the result
    def logResult(self):
        if sys.exc_info() == (None, None, None):
            self._browser.log(constants.TEST_PASS)
        else:
            self._browser.log(constants.TEST_FAIL)

if __name__ == '__main__':
    unittest.main()
