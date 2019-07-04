import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])
from browser import Browser
import time    

deraSCMUrl = "https://derapps-staging.azurewebsites.net/SCM"
tab_centre= "centre";
tab_preacher= "preacher";
lookup_sewadar ="sewadar";
group_no_centre = "2";
group_no_preacher = "4";
list_no_centre = "2"
list_no_preacher = "3"

class FiddleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        """Start web browser"""
        delay = 60
        command_executor = os.getenv("CMD_EXECUTOR","")
        self._browser = Browser(command_executor, delay)
        try:
            username = os.getenv("SITE_LOGIN_USER","")
            password = os.getenv("SITE_LOGIN_PWD","")
            self._browser.login_on_page(deraSCMUrl, username, password)
        except Exception as ex:
            self.fail(ex)
        
    def setUp(self):
        time.sleep(2)

    # Do Nothing
    def test_0(self):
        pass
    
    # This will test search the centre schedule
    def test_1_search_centre_scehdule(self):
        try:
            self._browser.test_search(tab_centre, group_no_centre, list_no_centre, "2", "ba")
        except Exception as ex:
            self.fail(ex)
    
    def test_2_search_centre_scehdule(self):
        try:
            self._browser.test_search_query(tab_centre, group_no_centre, list_no_centre, "1", "bangalore")
        except Exception as ex:
            self.fail(ex)
    
    # This will test export the centers
    def test_3_export_center(self):
        try:
            self._browser.test_export(tab_centre , group_no_centre , list_no_centre, "1")
        except Exception as ex:
            self.fail(ex)
    
    def test_4_search_preacher(self):
        try:
            self._browser.test_search_query(lookup_sewadar, group_no_preacher, list_no_preacher, "1", "GUL")
        except Exception as ex:
            self.fail(ex)
    
    # This will test export the preachers
    def test_5_export_preacher(self):
        try:
            self._browser.test_export(tab_preacher , group_no_preacher , list_no_preacher, "1")
        except Exception as ex:
            self.fail(ex)
    
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