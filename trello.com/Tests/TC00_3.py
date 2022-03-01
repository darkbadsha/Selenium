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

time.sleep(3)
Click_Login = driver.find_element(By.XPATH, login_locator.Longin)
Click_Login.click()

time.sleep(2)
space_dfa = driver.find_element(By.XPATH, login_locator.workspace_Dfa)
space_dfa.click()

time.sleep(1)
clk_Board = driver.find_element(By.XPATH, login_locator.Click_Boards)
clk_Board.click()

time.sleep(1)
Slt_Create = driver.find_element(By.XPATH, login_locator.Create)
Slt_Create.click()

time.sleep(1)
Write_title = driver.find_element(By.XPATH, login_locator.Title)
Write_title.send_keys('Demo Title')

time.sleep(2)
Slt_color = driver.find_element(By.XPATH, login_locator.Color_btn)
Slt_color.click()

time.sleep(2)
Clk_Btn = driver.find_element(By.XPATH, login_locator.Create_Btn)
Clk_Btn.click()

time.sleep(5)
driver.close()
