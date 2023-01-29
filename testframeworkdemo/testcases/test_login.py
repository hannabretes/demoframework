import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.start_page import StartPage

@pytest.mark.usefixtures("setup")
class TestLogin():
    def test_login(self):
        sp = StartPage(self.driver, self.wait)
        sp.click_to_login()