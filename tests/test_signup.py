import datetime

from browser import *
from test_case_class import TestCase
import prop
import random
import string
from signup import SignupPage
from my_account_page import MyAccountPage
from flaky import flaky
from selenium import webdriver
from datetime import datetime


class TestSignupPage(TestCase):
    def setUp(self):

        # self.driver = start_driver(
        #     command_executor=prop.webdriver_url,
        #     desired_capabilities=prop.support_browser[prop.browser])
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    @flaky
    def test_successful_signup(self):
        driver = self.driver
        go_to(driver,"https://magento.softwaretestingboard.com/")
        sleep(1)
        click_link_text(driver, "Create an Account")
        first_name_input = "testfirst"+ ''.join(random.choices(string.ascii_lowercase, k=4))
        last_name_input = "testlastname"+ ''.join(random.choices(string.ascii_lowercase, k=4))
        input_text(driver, SignupPage.first_name, first_name_input)
        input_text(driver, SignupPage.last_name, last_name_input)
        now = datetime.now()
        dt_string = now.strftime("%d%m%y%H%M")
        email = first_name_input + dt_string+"@gmail.com"
        input_text(driver, SignupPage.email_address, email )
        input_text(driver, SignupPage.password, "password1234!")
        input_text(driver, SignupPage.confirm_password, "password1234!")
        click(driver, SignupPage.create_an_account_button)
        sleep(1)
        self.assertTrue(MyAccountPage.page_title, "My Account")
        import pdb; pdb.set_trace()
        self.assertIn(email, return_text(driver, MyAccountPage.account_info))

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


