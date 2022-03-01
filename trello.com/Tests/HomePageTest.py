from Locators.Locators import LoginLocators
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement

class HomePageTest(object):
    def __init__(self, driver, base=""):
        self.base = base
        self.driver = driver
        self.timeout = 30
    def find_element(self,*locator)

    def find_all_element(self,*locator):
        return self.driver.LoginLocators(*locator)
