from browser import *
class SignupPage(object):
    first_name = ("input[name='firstname']", "css selector")
    last_name = ("#lastname", "css selector")
    email_address = ("input[name='email']", "css selector")
    password = ("#password", "css selector")
    confirm_password = ("#password-confirmation", "css selector")
    create_account = ("#form-validate > div > div.primary > button")
    create_an_account_button = (".action.submit.primary", "css selector")
    account_info = (".box-content>p", "css selector")
    home_logo = (".logo", "css selector")

    def sign_up(driver, first_name_input, last_name_input, email, password):
        click_link_text(driver, "Create an Account")
        input_text(driver, SignupPage.first_name, first_name_input)
        input_text(driver, SignupPage.last_name, last_name_input)
        input_text(driver, SignupPage.email_address, email)
        input_text(driver, SignupPage.password, password)
        input_text(driver, SignupPage.confirm_password, password)
        click(driver, SignupPage.create_an_account_button)
        sleep(1)



