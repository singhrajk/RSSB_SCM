#!/usr/bin/python
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import constants

class Browser:
    
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Browser.__instance == None:
            Browser()
        return Browser.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Browser.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            try:
                command_executor = os.getenv(constants.EXECUTOR,"")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-gpu')
                Browser.__instance = webdriver.Remote(
                        command_executor=command_executor,
                        desired_capabilities=chrome_options.to_capabilities()
                        )
            except WebDriverException as e:
                s = "%s" % e
                print ("Got exception %s" % s)
                print ("%s" % dir(s))
                if "Empty pool of VM for setup Capabilities" not in s:
                    raise
