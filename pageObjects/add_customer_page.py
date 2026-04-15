from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
import time

class Add_customer:
    customer_menu = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menu_item = "//a[@href='/Admin/Customer/List']"
    add_new_button = "//a[@href='/Admin/Customer/Create']"
    email_button = "//input[@id='Email']"
    password_button="//input[@id='Password']"
    first_name= "//input[@name='FirstName']"
    last_name="//input[@name='LastName]"
    gender_male= "//input[@id='Gender_Male']"
    gender_female= "//input[@id='Gender_Female']"


    customer_roles_xpath="//input[@role='searchbox']"
    cs_rl_administrator_xpath="//*[@id='select2-SelectedCustomerRoleIds-result-ym51-1']"
    cs_rl_guest_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-4mo6-4']"
    cs_rl_registered_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-a30h-3']"
    cs_rl_vendors_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-a30h-3']"

    manager_of_vendors_path="//span[@id='select2-VendorId-container']"

    active_option="//input[@id='Active']"
    customer_must_change_password="//input[@class='check-box' and @name='MustChangePassword']"
    admin_comment="//textarea[@id='AdminComment']"
    company_name= "//input[@id='Company']"
    save_button_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver=driver

    def click_on_customers_menu(self):
        self.driver.find_element(By.XPATH, self.customer_menu).click()
    
    def click_on_customer_menu_item(self):
        self.driver.find_element(By.XPATH, self.customer_menu_item).click()

    def click_on_add_new(self):
        self.driver.find_element(By.XPATH, self.add_new_button).click()

    def set_email(self, email):
        self.driver.find_elements(By.XPATH, self.email_button).clear()
        self.driver.find_elements(By.XPATH, self.email_button).send_keys(email)

    def set_password(self, password):
        self.driver.find_elements(By.XPATH, self.password_button).clear()
        self.driver.find_elements(By.XPATH, self.password_button).send_keys(password)

    def set_first_name(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name).send_keys(lastname)   

    def set_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.gender_male).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.gender_female).click()
        else:
            self.driver.find_element(By.XPATH, self.gender_male).click()

    def set_company_name(self, cmpname):
        self.driver.find_element(By.XPATH, self.company_name).send_keys(cmpname)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def manager_of_vendors(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.manager_of_vendors_path))
        drp.select_by_visible_text(value)

    def set_customer_roles(self, role):
        self.driver.find_element(By.XPATH, self.customer_roles_xpath).click()
        time.sleep(3000)
        if role == "Registered":
            self.lstitem = self.driver.find_elements(By.XPATH, self.cs_rl_registered_xpath)
        elif role == "Administrators":
            self.lstitem = self.driver.find_elements(By.XPATH, self.cs_rl_administrator_xpath)
        elif role == "Guests":
            #here user can be registered or guest, only one can select not both will fit
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            self.lstitem = self.driver.find_elements(By.XPATH, self.cs_rl_guest_xpath)
        elif role == "Registered":
            self.lstitem = self.driver.find_elements(By.XPATH, self.cs_rl_registered_xpath)
        elif role == "Vendors":
            self.lstitem = self.driver.find_element(By.XPATH, self.cs_rl_vendors_xpath)
        else : 
            self.lstitem = self.driver.find_element(By.XPATH, self.cs_rl_guest_xpath)
        time.sleep(5000)
        self.driver.execute_script("arguments[0].click()", self.lstitem)




    