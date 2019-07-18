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
    
    # This will test search the centre schedule
    def test_1_Centre_Search_Schedule(self):
        try:
            Centre("ba").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)

    # This will search a particular centre details
    def test_2_Centre_Search_Centre_Details(self):
        try:
            Centre("bangalore").query_search()
        except Exception as ex:
            self.fail(ex)
    
    # This will delete centre details
    def test_3_Centre_Delete_Centre_Details(self):
        try:
            Centre("Gawla").delete(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will insert centre details
    def test_4_Centre_Insert_Centre_Details(self):
        try:
            Centre("Gawla").insert()
        except Exception as ex:
            self.fail(ex)

    # This will test export the centers
    def test_5_Centre_Export_Centre_Details(self):
        try:
            Centre().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)
    
    # This will search a sewadar
    def test_6_Preacher_Search_Sewadar_Details(self):
        try:
            Preacher("GUL").query_search()
        except Exception as ex:
            self.fail(ex)

    # This will test export the preachers
    def test_7_Preacher_Export_Preacher_Details(self):
        try:
            Preacher().export(constants.CHOICE_1)
        except Exception as ex:
            self.fail(ex)   
    
    # This will test search the preacher language
    def test_8_Preacher_Preacher_Language(self):
        try:
            Preacher("GUL").search(constants.CHOICE_2)
        except Exception as ex:
            self.fail(ex)
    
if __name__ == '__main__':
    unittest.main()