import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from demoframework.testframeworkdemo.pages.start_page import StartPage
from demoframework.testframeworkdemo.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin():
    def test_login(self):
        sp = StartPage(self.driver, self.wait)
        lp = LoginPage(self.driver, self.wait)
        sp.click_to_login()
        lp.input_data_login()