from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from authentication.tests import AuthTestCase

class AdminTestCase(StaticLiveServerTestCase):


    def setUp(self):
        #Load base test functionality for decide
        self.auth = AuthTestCase()
        self.auth.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
        self.auth.tearDown()

    def test_simpleCorrectLogin(self):
        self.driver.get(f'{self.live_server_url}/admin/')
        self.driver.find_element(By.XPATH, "//input[@id=\'id_username\']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@id=\'id_password\']").send_keys("qwerty",Keys.ENTER)

        print(self.driver.current_url)
        #In case of a correct loging, a element with id 'user-tools' is shown in the upper right part
        self.assertTrue(len(self.driver.find_elements(By.XPATH, "//div[@id=\'header\']"))==1)