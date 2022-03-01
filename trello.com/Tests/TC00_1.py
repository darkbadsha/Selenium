from Locators.Locators import LoginLocators
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
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

time.sleep(1)
Click_Login = driver.find_element(By.XPATH, login_locator.Longin)
Click_Login.click()

time.sleep(2)
Click_plsBtn = driver.find_element(By.XPATH, login_locator.PlusBtn)
Click_plsBtn.click()

time.sleep(1)
Work_OF = driver.find_element(By.XPATH, login_locator.MirazOfc)
Work_OF.send_keys("MirazOffice")

time.sleep(2)
Work_type = driver.find_element(By.XPATH, login_locator.Work_types)
Work_type.click()

time.sleep(5)
Click_btn = driver.find_element(By.XPATH, login_locator.SelectWork)
ActionChains(driver).perform()

time.sleep(2)
slt_it = driver.find_element(By.XPATH, login_locator.Slt_iT)
slt_it.click()

time.sleep(1)
Write_description = driver.find_element(By.XPATH, login_locator.Description)
Write_description.send_keys("We all work together")

time.sleep(1)
Click_Continue = driver.find_element(By.XPATH, login_locator.Continue)
Click_Continue.click()

time.sleep(1)
I_ll_do_This_latter = driver.find_element(By.XPATH, login_locator.Click_Do_later)
I_ll_do_This_latter.click()

time.sleep(5)
driver.quit()
