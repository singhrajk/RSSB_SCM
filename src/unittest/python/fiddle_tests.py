import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
from browser import Browser
import time

def test_export(browser, tab, group_no, list_no, choice_no):
    browser.select_group(group_no , tab)
    browser.select_group_choice(list_no,choice_no)
    browser.query_records(tab)
    browser.fetch_records(tab)
    browser.export_records_in_excel(tab)

class FiddleTest(unittest.TestCase):

    def setUp(self):
        """Start web browser"""
        command_executor = os.getenv("CMD_EXECUTOR","")
        delay = 60
        self._browser = Browser(command_executor, delay)

    def test_login_and_export_center(self):
        try:
            url = "https://derapps-staging.azurewebsites.net/SCM"
            username = os.getenv("SITE_LOGIN_USER","")
            password = os.getenv("SITE_LOGIN_PWD","")
            self._browser.login_on_page(url, username, password)
            test_export(self._browser, "Center" , "2" , "2", "1")
            time.sleep(2)
        except Exception as ex:
            self.fail(ex)

    def test_login_and_export_preacher(self):
        try:
            url = "https://derapps-staging.azurewebsites.net/SCM"
            username = os.getenv("SITE_LOGIN_USER","")
            password = os.getenv("SITE_LOGIN_PWD","")
            self._browser.login_on_page(url, username, password)
            test_export(self._browser, "Preacher" , "4" , "3", "1")
            time.sleep(2)
        except Exception as ex:
            self.fail(ex)
