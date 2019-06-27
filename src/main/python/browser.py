#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import os

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

    def load_page_in_browser(self, url, errorMsg):
        try:
            self._browser.get(url)
        except:
            print (errorMsg)

    def get_element_from_xpath(self, xpath, element_present):
            WebDriverWait(self._browser, self._delay).until(element_present)
            time.sleep(1)
            element = self._browser.find_element_by_xpath(xpath)
            return element

    def get_element_wait_for_presence(self, xpath):
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            return self.get_element_from_xpath(xpath, element_present)

    def get_element_wait_for_clickable(self, xpath):
            element_present = EC.element_to_be_clickable((By.XPATH, xpath))
            return self.get_element_from_xpath(xpath, element_present)

    def send_inputs_at_xpath(self, xpath, keys, errorMsg):
        try:
            element = self.get_element_wait_for_presence(xpath)
            element.send_keys(keys)
        except:
            print (errorMsg)

    def click_element_at_xpath(self, xpath, errorMsg):
        try:
            try:
                element = self.get_element_wait_for_presence(xpath)
            except:
                element = self.get_element_wait_for_clickable(xpath)
            finally:
                element.click()
        except:
            print (errorMsg)

    def select_group(self, group_no, tab):
        self.click_element_at_xpath('//*[@id="mnugrp_' + group_no + '"]', "Error while clicking: " + tab + " tab")

    def select_group_choice(self, list_no, choice_no):
        self.click_element_at_xpath('//*[@id="wdf_root_div_id"]/div[1]/div/div[1]/ul/li[' + list_no + ']/ul/li[' + choice_no + ']/span/span[1]', "Error while clicking Centre Choice")

    def query_records(self, tab):
        self.click_element_at_xpath('//*[@id="btnQuery"]/i',"Error while quering: " + tab + " tab")

    def fetch_records(self, tab):
        self.click_element_at_xpath('//*[@id="btnGet"]',"Error while fetching records for: " + tab + " tab")

    def export_records_in_excel(self, tab):
        self.click_element_at_xpath('//*[@id="wdf-list-view row-fluid"]/div/div[1]/div/button', "Error while exporting : " + tab + " tab")

    def login_on_page(self, url, username, password):
        self.load_page_in_browser(url, "Error Loading the page")
        self.send_inputs_at_xpath('//*[@id="LoginId"]', username, "User Id Error")
        self.send_inputs_at_xpath('//*[@id="Password"]', password, "Password Error" )
        self.click_element_at_xpath('//*[@id="login-button"]',"Submit Error")

def main():
    command_executor = os.getenv("CMD_EXECUTOR","")
    delay = 60
    browser = Browser(command_executor, delay)

    url = "https://derapps-staging.azurewebsites.net/SCM"
    username = os.getenv("SITE_LOGIN_USER","")
    password = os.getenv("SITE_LOGIN_PWD","")
    browser.login_on_page(url, username, password)
    time.sleep(10)

if __name__ == "__main__":
    main()
