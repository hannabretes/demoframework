from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from demoframework.testframeworkdemo.pages.base_page import BasePage


class LoginPage(BasePage):
    emailinput = (By.XPATH, '//input[@placeholder="Email"]')
    passwordinput = (By.XPATH, '//input[@placeholder="Password"]')
    loginbutton = (By.XPATH, '//button[normalize-space()="Login"]')
    def __init__(self,driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait
    def input_data_login(self):
        self.do_send_keys(self.emailinput,"su-35@wp.pl")
        self.do_send_keys(self.passwordinput,"Pol@nie2")
        self.do_click(self.loginbutton)
        time.sleep(5)