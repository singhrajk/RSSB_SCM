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

class TabTest(unittest.TestCase):

    # Method getting the test name
    def getTestName(self):
        testMethodName = re.sub(constants.TEST_NUMBER_PATTERN, constants.EMPTY, self._testMethodName, 1)
        return testMethodName.replace(constants.UNDERSCORE, constants.SPACE)

    # setup method, called once before all the tests
    @classmethod
    def setUpClass(self):

        username = os.getenv(constants.USERNAME,"")
        password = os.getenv(constants.PASSWORD,"")
        """Start web browser"""
        self._home_page = Tab()
        # self._home_page.login_on_page(constants.DERA_SCM_URL, username, password)

    # setup method, called before each test
    def setUp(self):
        time.sleep(2)
        self._home_page.log(constants.STARS_START_LINE)
        self._home_page.log(constants.TEST_START  + self.getTestName())


    def test_0_load_page_in_browser_invalid_url(self):
        with self.assertRaises(Exception) as context:
            url = "derapps-staging.azurewebsites.net/SCM"
            self._home_page.load_page_in_browser(url)

        self.assertTrue('Error Loading URL : {}'.format(url) in context.exception)

    # This will run at end of each test
    def tearDown(self):
        self._home_page.log(constants.TEST_FINSIH  + self.getTestName())
        self.logResult()
        self._home_page.log(constants.STARS_END_LINE)

    # This will run at end of all tests
    @classmethod
    def tearDownClass(self):
        """Logout browser"""
        # try:
        #     time.sleep(2)
        #     self._home_page.logout();
        # except Exception as ex:
        #     self.fail(ex)
        # time.sleep(4)
        self._home_page = None

    # Method to log the result
    def logResult(self):
        if sys.exc_info() == (None, None, None):
            self._home_page.log(constants.TEST_PASS)
        else:
            self._home_page.log(constants.TEST_FAIL)

if __name__ == '__main__':
    unittest.main()
