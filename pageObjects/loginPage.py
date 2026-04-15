from selenium.webdriver.common.by import By
import time

class Loginpage:
    textbox_username_id="//input[@id='Email']"
    textbox_password_id="//input[@id='Password']"
    button_login_xapth="//button[normalize-space()='Log in']"
    link_logout_linktext = "logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xapth).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_linktext).click()