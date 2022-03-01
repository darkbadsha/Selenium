from selenium.webdriver.common.by import By


class LoginLocators:
    # LoginPage elements
    login_btn = (By.XPATH, '/html/body/header/nav/div/a[1]')
    Email = (By.XPATH, '/html/body/div[1]/section/div/div/div[4]/form/div/div/div[1]/input')
    login_click = (By.XPATH, '/html/body/div[1]/section/div/div/div[4]/form/div/div/input')
    password = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/div/div/input')
    Longin = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/button/span")
    PlusBtn = (By.XPATH, '/html/body/div/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/ul/div/button/span/span/span')
    MirazOfc = (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/form/input")
    Work_types = (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/form/div/div/div/div")
    SelectWork = (By.XPATH, '//*[@id="layer-manager-overlay"]/div/div/div/div/div[1]/form/div/div/div/div/div[1]/div')
    Slt_iT = (By.XPATH, '//*[@id="layer-manager-overlay"]/div/div/div/div/div[1]/form/div/div/div/div/div[1]/div')
    Description = (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/form/textarea")
    Continue = (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/form/footer/button")
    Click_Do_later = (By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/a")
    Prl_temp = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/ul/li[7]/a')
    Board = (By.XPATH, '/html/body/div/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/li[1]/a/span[2]')
    First_Board = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/button')
    workspace_Dfa = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/ul/li[1]/a')
    Click_Boards = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[1]/nav/div[2]/div/ul/li[1]/ul/li[1]/a/span[2]')
    Create = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/ul/li[2]/div/p/span')
    Title = (By.XPATH, '/html/body/div[2]/div/section/div/form/div[1]/label/input')
    Dfa = (By.XPATH, '//*[@id="1645758272897-create-board-select-team"]/div/div/div[1]/div')
    Color_btn = (By.XPATH, '//*[@id="background-picker"]/ul[2]/li[3]/button')
    Create_Btn = (By.XPATH, '/html/body/div[2]/div/section/div/form/button')
    Get_start = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[11]/div/a/button')
    Template = (By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/a/span[2]')
    Select_Templates = (By.XPATH,  "/html/body/div/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/a/span[2]")

class View_Personal_template:
    login_btn = '/html/body/header/nav/div/a[1]'
    Email = '/html/body/div[1]/section/div/div/div[4]/form/div/div/div[1]/input'
    login_click = '/html/body/div[1]/section/div/div/div[4]/form/div/div/input'
    password = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[2]/div/div/div/div/div/input'
    Longin = "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/button/span"
    Template = '//*[@id="content"]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/a/span[2]'
    Education = "/html/body/div/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/ul/li[3]/a/span"
    Select_Templates = "/html/body/div/div[2]/div[1]/div/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[1]/ul/div/li/a/span[2]"
    Click_Temp = '//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/a/div[3]/div[2]/div'
