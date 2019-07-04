#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time

waitForPresence = 1
waitForClickable = 2
waitForPresenceAndClickable = 3

class Browser():
    def __init__(self, command_executor, delay):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            self._browser = webdriver.Remote(
                command_executor=command_executor,
                desired_capabilities=chrome_options.to_capabilities()
            )
        except WebDriverException as e:
            s = "%s" % e
            print("Got exception %s" % s)
            print("%s" % dir(s))
            if "Empty pool of VM for setup Capabilities" not in s:
                raise
        self._delay = delay

    def __del__(self):
      self._browser.quit()

        # Load a particular page in the browser
    def load_page_in_browser(self, url, errorMsg):
        try:
            self._browser.get(url)
        except:
            print (errorMsg)
    
    # Get Element From XPath after when the element is present
    def get_element_from_xpath(self, xpath, wait):
        if wait == waitForPresence:
                WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        elif wait == waitForClickable:
                WebDriverWait(self._browser, self._delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elif wait == waitForPresenceAndClickable:
                WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
                WebDriverWait(self._browser, self._delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        time.sleep(1)
        element = self._browser.find_element_by_xpath(xpath)
        return element

    # Sends Input keys at a particular input on x path after it is present
    def send_inputs_at_xpath(self, xpath, keys, errorMsg):
        try:
            element = self.get_element_from_xpath(xpath, waitForPresence)
            element.send_keys(keys)
        except:
            print (errorMsg)
        
    # Click the element available at the X Path after it is Present & Clickable
    def click_element_at_xpath(self, xpath, errorMsg):
        try:
            element = self.get_element_from_xpath(xpath, waitForPresenceAndClickable)
            element.click()
        except:
            print (errorMsg)
            
    # Select group on the screen
    def select_group(self, group_no, tab):
        self.click_element_at_xpath('//*[@id="mnugrp_' + group_no + '"]', "Error while clicking: " + tab + " tab")
    
    # Select the element in the list, Put the list_no as the position of the tab, put the choice_no as the position of the element
    def select_group_choice(self, list_no, choice_no):
        self.click_element_at_xpath('//*[@id="wdf_root_div_id"]/div[1]/div/div[1]/ul/li[' + list_no + ']/ul/li[' + choice_no + ']/span/span[1]', "Error while clicking Centre Choice")
    
    def select_group_and_group_choice(self, tab, group_no, list_no, choice_no): 
        self.select_group(group_no , tab)
        self.select_group_choice(list_no, choice_no)    
    
    # Query the records, this will press the Query Button
    def query_records(self, tab):
        self.click_element_at_xpath('//*[@id="btnQuery"]/i',"Error while quering: " + tab + " tab")
    
    # Fetch the records, this will press the Get button
    def fetch_records(self, tab):
        self.click_element_at_xpath('//*[@id="btnGet"]',"Error while fetching records for: " + tab + " tab")
    
    # This will click on the export button on browser
    def export_records_in_excel(self, tab):
        self.click_element_at_xpath('//*[@id="wdf-list-view row-fluid"]/div/div[1]/div/button', "Error while exporting : " + tab + " tab")
    
    def search_input(self, tab, search_input):
        self.send_inputs_at_xpath('//*[@id="'+tab+'_Id_lookup"]',search_input, "Error while entering data to search " + tab + " tab")
    
    def click_select_button (self, tab):
        self.click_element_at_xpath('//*[@id="divOptions"]/button',"Error while clicking select button: " + tab + " tab")
    
    def click_search_button (self, tab):
        self.click_element_at_xpath('//*[@id="wdfScreenFieldSet"]/div/div/form/div[1]/fieldset/button',"Error while clicking search button: " + tab + " tab")
    
    # This method is to login on page, username , password will come from environment
    def login_on_page(self, url, username, password):
        self.load_page_in_browser(url, "Error Loading the page")
        self.send_inputs_at_xpath('//*[@id="LoginId"]', username, "User Id Error")
        self.send_inputs_at_xpath('//*[@id="Password"]', password, "Password Error" )
        self.click_element_at_xpath('//*[@id="login-button"]',"Login Submit Error")
    
    # Method to test the export
    def test_export(self, tab, group_no, list_no, choice_no):
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.query_records(tab)
        self.fetch_records(tab)
        self.export_records_in_excel(tab)
    
    def test_search(self, tab, group_no, list_no, choice_no, search_input):
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.search_input(tab, search_input)
        time.sleep(1)
        self.click_select_button(tab)
        self.click_search_button(tab)
        
    def logout(self):
        self.click_element_at_xpath('//*[@id="wdf_root_div_id"]/div[1]/div/div[2]/div/div[2]/a[2]',"Logout Error")
    
    def test_search_query(self, tab, group_no, list_no, choice_no, search_input):
        self.select_group_and_group_choice(tab, group_no, list_no, choice_no)
        self.query_records(tab)
        self.search_input(tab, search_input)
        self.click_select_button(tab)
        self.fetch_records(tab)