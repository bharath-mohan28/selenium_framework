import pytest 
from selenium import webdriver
from pageObjects.loginPage import Loginpage
from utilities.read_properties import Readconfig
from utilities.custom_logger import Log_generation
from utilities import excel_utils
import time

#for every test case the naming convection should be class Test_{tc_no}_{name} ex: Test_001_login

class Test_002_DDT:
    base_url = Readconfig.get_application_url()
    path = ".//test_data/LoginData.xlsx"
    logger = Log_generation.loggen()

    def test_login_ddd(self, setup):
        self.logger.info("************Test_002_DDT_test**************")
        self.logger.info("************Verify Login Test**************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)

        self.rows = excel_utils.get_row_count(self.path, 'Sheet1')
        print("Number of roles in the Excel Sheet",self.rows)


        lst_status= []
        for r in range (2,self.rows + 1):
            self.user = excel_utils.read_data(self.path, 'Sheet1',r,1)
            self.password = excel_utils.read_data(self.path, 'Sheet1',2)
            self.exp = excel_utils.read_data(self.path, 'Sheet1',r, 3)
             
        self.lp.setUserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(5)

        actual_title = self.driver.title
        self.driver.close()
        exp_title =  "Dashboard / nopCommerce administration"
        if actual_title == exp_title:
            if self.exp == "Pass":
                self.logger("*********passed************")
                self.lp.ClickLogout();
                lst_status.append("Pass")
            elif self.exp == "Fail":
                self.logger.info("******failed*********")
                self.lp.ClickLogout();
                lst_status.append("Fail")
        elif actual_title != exp_title:
            if self.exp =='Pass':
                self.logger.info("*******Fail*********")
                lst_status.append("Fail")
            elif self.exp == 'Fail':
                self.logger.info("***********passed******")
                lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test is Passed")
        else:
            self.logger.info("login DDt test is Failed")

        self.logger.info("************End of Login test ***************")
        self.logger.info ("*******************completed*****************************")

           


            
