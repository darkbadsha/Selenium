from Locators.Locators import LoginLocators
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement

driver = webdriver.Chrome("C:\\Users\\asif.rouf\\PycharmProjects\\trello.com\\drive\\chromedriver.exe")
driver.maximize_window()
driver.get("https://trello.com/home")
login_locator = LoginLocators()

login_button = driver.find_element(By.XPATH, login_locator.login_btn)
time.sleep(2)
login_button.click()

time.sleep(1)
enter_email = driver.find_element(By.XPATH, login_locator.Email)
enter_email.send_keys("task.axbd@gmail.com")

time.sleep(2)
login_click = driver.find_element(By.XPATH, login_locator.login_click)
login_click.click()

time.sleep(2)
enter_password = driver.find_element(By.XPATH, login_locator.password)
enter_password.send_keys("1234567891")

time.sleep(2)
Click_Login = driver.find_element(By.XPATH, login_locator.Longin)
Click_Login.click()

time.sleep(2)
S_Template = driver.find_element(By.XPATH, login_locator.Select_Templates)
S_Template.click()

time.sleep(3)
Clk_Personal = driver.find_element(By.XPATH, login_locator.Prl_temp)
Clk_Personal.click()

time.sleep(5)
driver.close()
print("pass")