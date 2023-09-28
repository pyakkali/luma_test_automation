from browser import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage(object):
    email = ("input[id='email']", "css selector")
    password = ("input[id='pass']", "css selector")
    signin = (".action.login.primary", "css selector")


    def login(driver, email_input, password_input):

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((SignInPage.email[1], SignInPage.email[0])))
        input_text(driver, SignInPage.email, email_input)
        input_text(driver, SignInPage.password, password_input)
        click(driver, SignInPage.signin)

