import unittest
import sys
import os
BASE_PATH = os.getenv('SCM_HOME',"")
sys.path.extend([BASE_PATH + '/src/main/python/'])

from TestBase import TestBase
from Centre import Centre
from Preacher import Preacher
import constants

class FiddleTest(TestBase):
    
    # This will delete centre details
    def test_1_Centre_Delete(self):
        try:
            Centre("Gawla").delete(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will insert centre details using tab
    def test_2_Centre_Insert(self):
        try:
            Centre("Gawla").insert()
        except Exception as ex:
            self.fail(ex)
            
    # This will search a particular centre details and check the details are inserted using x path
    def test_3_Centre_Search(self):
        try:
            Centre("Gawla").query_search()
        except Exception as ex:
            self.fail(ex)     

    # This will update the centre details using shift reverse tab(shift + tab) and test the details are updated using x path
    def test_4_Centre_Update(self):
        try:
            # Centre("Gawla").update() 
            pass
        except Exception as ex:
            self.fail(ex)     
    
    # This will test export the centers
    def test_5_Centre_View_Export(self):
        try:
            Centre().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will test search the centre schedule
    def test_6_Centre_Schedule_Search(self):
        try:
            Centre("ba").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)

    # This will search a sewadar
    def test_7_Preacher_Profile_Search(self):
        try:
            Preacher("GUL").query_search()
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    def test_8_Preacher_Profile_View_Export(self):
        try:
            Preacher().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)   
    
    # This will test search the preacher language
    def test_9_Preacher_Language_Search(self):
        try:
            Preacher("GUL").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)
    
if __name__ == '__main__':
    unittest.main()
