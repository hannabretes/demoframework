from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class StartPage(BasePage):
    myaccountbutton = (By.XPATH, '//ul[@class="nav navbar-nav navbar-right hidden-sm go-left"]//a[@class="dropdown-toggle go-text-right"][normalize-space()="My Account"]')
    loginbutton = (By.XPATH, '//ul[@class="nav navbar-nav navbar-right hidden-sm go-left"]//ul[@class="nav navbar-nav navbar-side navbar-right sidebar go-left user_menu"]//li[@id="li_myaccount"]//ul[@class="dropdown-menu"]//li//a[@class="go-text-right"][normalize-space()="Login"]')
    def __init__(self,driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait
    def click_to_login(self):
        self.do_click(self.myaccountbutton)
        self.do_click(self.loginbutton)
        time.sleep(5)
