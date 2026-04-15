import string
import random
from utilities.read_properties import Readconfig
from utilities.custom_logger import Log_generation
from pageObjects.loginPage import Loginpage
from pageObjects.add_customer_page import Add_customer
import pytest 
import time

class Test_002_add_customer_details:
    base_url = Readconfig.get_application_url()
    username = Readconfig.get_application_useremail()
    password = Readconfig.get_application_password()
    logger = Log_generation.loggen()

    def random_generator(size = 8, char = string.ascii_lowercase + string.digits):
        return ''.join(random.choice(char) for x in range(size))

    def test_add_customer(self, setup):
        self.logger.info("*****************Test_002_add_customer_details****************************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()

        self.logger.info("*****Login Successfull**********")
        self.logger.info("**********Started  Add Customer test*********************")

        self.addcust = Add_customer(self.driver)
        self.addcust.click_on_customers_menu()
        self.addcust.click_on_customer_menu_item()

        self.email = self.random_generator()+"@gmail.com"
        self.addcust.set_email(self.email)
        self.addcust.set_password("test123")
        self.addcust.set_company_name("NetradyneQa")
        self.addcust.set_customer_roles("Guests")
        self.addcust.set_gender("Male")
        self.addcust.manager_of_vendors("Vendor 2")
        self.addcust.set_first_name("bharath")
        self.addcust.set_last_name("M")
        self.addcust.click_on_save()
        self.logger.info("***********Saving Customer data")


