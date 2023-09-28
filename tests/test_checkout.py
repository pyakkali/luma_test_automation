import datetime

from browser import *
from test_case_class import TestCase
import prop
import random
import string
from signup import SignupPage
from products_page import ProductPage
from signin import SignInPage
from signup import SignupPage
from product_detail_page import ProductDetailPage
from my_account_page import MyAccountPage
from flaky import flaky
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
import pytest


class TestCheckout(TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    # @pytest.mark.skip
    @flaky
    def test_new_user_checkout(self):
        driver = self.driver
        go_to(driver, "https://magento.softwaretestingboard.com/")
        first_name_input = "testfirst" + ''.join(random.choices(string.ascii_lowercase, k=4))
        last_name_input = "testlastname" + ''.join(random.choices(string.ascii_lowercase, k=4))
        now = datetime.now()
        dt_string = now.strftime("%d%m%y%H%M")
        email = first_name_input + dt_string + "@gmail.com"
        password = "password1234!"
        SignupPage.sign_up(driver, first_name_input, last_name_input, email, password)
        click(driver, SignupPage.home_logo)
        click_link_text(driver, "Women")
        sleep(1)
        click_link_text(driver, "Jackets")
        sleep(1)
        click(driver, ProductPage.product_list, idx=1)
        product_price = return_text(driver, ProductDetailPage.product_price)
        ProductDetailPage.select_product_size(driver, size="M")
        click(driver, ProductDetailPage.green_color)
        click(driver, ProductDetailPage.add_to_cart)
        sleep(2)
        self.assertEqual(return_text(driver, ProductDetailPage.cart_count), "1")
        click(driver, ProductDetailPage.cart_count)
        wait_for_element_to_be_visible(driver, ProductDetailPage.proceed_to_checkout)
        click(driver, ProductDetailPage.proceed_to_checkout)
        wait_for_element_to_be_visible(driver, ProductDetailPage.address_0)
        input_text(driver, ProductDetailPage.address_0, "1808 S Pacific Coast Hwy")
        input_text(driver, ProductDetailPage.city, "Redondo Beach")
        select = Select(get_element(driver, ProductDetailPage.state))
        # select by visible text
        select.select_by_visible_text('California')
        input_text(driver, ProductDetailPage.zip, "90277")
        select = Select(get_element(driver, ProductDetailPage.country))
        # select by visible text
        select.select_by_visible_text('United States')
        input_text(driver, ProductDetailPage.phone, "2013337070")
        click(driver, ProductDetailPage.standard_ship_method)
        click(driver, ProductDetailPage.next_button)
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_price)
        #verify total price
        self.assertTrue(return_text(driver, ProductDetailPage.checkout_price), product_price)
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_ship_method)
        self.assertTrue(return_text(driver, ProductDetailPage.checkout_ship_method), "Best Way - Table Rate")
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_button)
        click(driver, ProductDetailPage.checkout_button)
        wait_for_element_to_be_visible(driver, ProductDetailPage.confirm_msg)
        self.assertTrue(return_text(driver, ProductDetailPage.confirm_msg), "Thank you for your purchase!")

    @flaky
    def test_existing_user_checkout(self):
        driver = self.driver
        go_to(driver, "https://magento.softwaretestingboard.com/")
        click_link_text(driver, "Sign In")
        SignInPage.login(driver, "testfirstkdia2309230946@gmail.com", "password1234!")
        sleep(1)
        try:
            click(driver, ProductDetailPage.cart_count)
            click(driver, ProductDetailPage.delete_cart)
            click(driver, ProductDetailPage.delete_popup_ok)
            sleep(1)
        except:
            pass
        click_link_text(driver, "Women")
        sleep(1)
        click_link_text(driver, "Jackets")
        click(driver, ProductPage.product_list, idx=1)
        product_price = return_text(driver, ProductDetailPage.product_price)
        ProductDetailPage.select_product_size(driver, size="M")
        click(driver, ProductDetailPage.green_color)
        click(driver, ProductDetailPage.add_to_cart)
        sleep(2)
        self.assertEqual(return_text(driver, ProductDetailPage.cart_count), "1")
        click(driver, ProductDetailPage.cart_count)
        # sleep(1)
        wait_for_element_to_be_visible(driver, ProductDetailPage.proceed_to_checkout)
        click(driver, ProductDetailPage.proceed_to_checkout)
        wait_for_element_to_be_visible(driver, ProductDetailPage.standard_ship_method)
        click(driver, ProductDetailPage.standard_ship_method)
        wait_for_element_to_be_visible(driver, ProductDetailPage.next_button)
        click(driver, ProductDetailPage.next_button)
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_price)
        self.assertTrue(return_text(driver, ProductDetailPage.checkout_price), product_price)
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_ship_method)
        self.assertTrue(return_text(driver, ProductDetailPage.checkout_ship_method), "Best Way - Table Rate")
        wait_for_element_to_be_visible(driver, ProductDetailPage.checkout_button)
        click(driver, ProductDetailPage.checkout_button)
        sleep(1)
        self.assertTrue(return_text(driver, ProductDetailPage.confirm_msg), "Thank you for your purchase!")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


