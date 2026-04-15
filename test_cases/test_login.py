import pytest 
from selenium import webdriver
from pageObjects.loginPage import Loginpage
from utilities.read_properties import Readconfig
from utilities.custom_logger import Log_generation

#for every test case the naming convection should be class Test_{tc_no}_{name} ex: Test_001_login

class Test_001_login:
    base_url = Readconfig.get_application_url()
    username = Readconfig.get_application_useremail()
    password = Readconfig.get_application_password()

    logger = Log_generation.loggen()

    def test_home_page_title(self,setup):
        self.logger.info("******************Test_001_Login***************************")
        self.logger.info("******************verifying the test case*******************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        # if act_title == "Your store. Login":
        #     assert True
        #     self.logger.info("**********Test case is Passed*************")
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
        #     self.driver.close()
        #     self.logger.info("************Test case failed*************")
        #     assert False
    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("************Verify Login Test**************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        actual_title = self.driver.title
        self.driver.close()
        # if actual_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.logger.info("Login title is validates correctly")
        # else:
        #     assert False
        #     self.logger.info("Login is failed")

    


            
