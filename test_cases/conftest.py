from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def setup(browser):
    try:
        chrome_options = Options()

        prefs = {"profile.password_manager_leak_detection":False, "credentials_enable_service":False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        
        if browser == 'chrome':
            driver = webdriver.Chrome(options=chrome_options)
            print("Launching Chrome Browser")
        elif browser == 'firefox':
            driver = webdriver.Firefox()
            print("Launching Firefox Browser")
        elif browser == 'safari':
            driver = webdriver.Safari()
            print("Launching Safari Browser")
        elif browser == 'ie':
            driver = webdriver.Ie()
            print("Launching Internet Explorer")
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    except WebDriverException as e:
        print(f"Error initializing the browser driver: {e}")
        raise
    except ValueError as ve:
        print(ve)
        raise

    yield driver
    driver.quit()

def pytest_addoption(parser): # this will get the valuses from the CLI/Hooks
    parser.addoption("--browser",action = "store", default = "chrome")

@pytest.fixture()
def browser(request):  #this will return the browser value to the setup method
    return request.config.getoption("--browser")