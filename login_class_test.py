import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"


class CreateAccountAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.skip_engine_check())

    def skip_engine_check(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")

        return self.chrome_options

    def open_sign_website(self, url):
        self.url = url
        self.driver.get(url)

    def close_browser(self):
        self.driver.close()

    def fill_username(self, username):
        self.username = username
        username_placeholder = self.driver.find_element(By.ID, "user-name")
        username_placeholder.send_keys(username)

    def fill_password(self, password):
        self.password = password
        password_placeholder = self.driver.find_element(By.ID, "password")
        password_placeholder.send_keys(password)

    def log_in(self):
        log_in_button = self.driver.find_element(By. ID, "login-button")
        log_in_button.click()

    def check_login(self):
        shopping_cart = self.driver.find_element(By. ID, "shopping_cart_container")
        if shopping_cart.is_displayed():
            print("Test passed, logged in successfully")
        else:
            print("something went wrong.")



obj1 = CreateAccountAutomation()
obj1.open_sign_website("https://www.saucedemo.com")
obj1.fill_username(username)
obj1.fill_password(password)
obj1.log_in()
obj1.check_login()