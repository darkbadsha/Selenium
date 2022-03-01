def login_button:
login_button = find_element(login_locator.login_btn)
time.sleep(2)
login_button.click()

time.sleep(1)
enter_email = find_element( login_locator.Email)
enter_email.send_keys("task.axbd@gmail.com")

time.sleep(2)
login_click = driver.find_element(login_locator.login_click)
login_click.click()

time.sleep(2)
enter_password = driver.find_element(By.XPATH, login_locator.password)
enter_password.send_keys("1234567891")

time.sleep(2)
Click_Login = driver.find_element(By.XPATH, login_locator.Longin)
Click_Login.click()

time.sleep(3)
Clk_Brd = driver.find_element(By.XPATH, login_locator.Board)
Clk_Brd.click()

time.sleep(1)
Crt_first_board = driver.find_element(By.XPATH, login_locator.First_Board)
Crt_first_board.click()

time.sleep(5)
driver.close()
