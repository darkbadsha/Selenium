
from Locators.Locators import LoginLocators
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from selenium import webdriver

from Tests.TC00_7 import TC00_7


class BasePage(TC00_7):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\asif.rouf\\PycharmProjects\\trello.com\\drive\\chromedriver.exe")
        cls.driver.maximize_window()

        cls.driver.get("https://trello.com/home")
 print("Test Started")