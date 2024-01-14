from pathlib import Path
from selenium import webdriver
from selenium.common import StaleElementReferenceException, UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

_MAX_WAIT_FOR_RETRIES = 3
DEFAULT_WAIT = 5
_WAIT_FOR_TIMEOUT = 30


class BaseClass(object):
    baseURL = "https://adnabu-arjun.myshopify.com/"
    print("baseURL:", baseURL)
    utils_path = Path(__file__).parents[1]
    path = str(utils_path) + "/driver/chromedriver_mac64/chromedriver"

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        service = Service(executable_path=cls.path)
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)

        cls.driver.maximize_window()
        cls.driver.get(cls.baseURL)

    @classmethod
    def browser_close(cls):
        cls.driver.close()

    def wait_for_element_with_xpath(self, selector):
        for x in range(0, _MAX_WAIT_FOR_RETRIES):
            try:
                WebDriverWait(self.driver, _WAIT_FOR_TIMEOUT).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, selector)),
                    'Could not find element {}'.format(selector)
                )
                return self.driver.find_element(By.XPATH, selector)
            except (StaleElementReferenceException, UnexpectedAlertPresentException):
                pass

    def wait_for_element_with_xpath_and_click(self, selector):
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.XPATH, selector)),
                'Could not find element {}'.format(selector)
            )
            element = self.driver.find_element(By.XPATH, selector)
            element.click()
        except:
            pass

    def go_to_url(self, url):
        self.driver.get(url)

