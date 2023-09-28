from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start_driver(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=None):
    for _ in range(1):
        try:
            return webdriver.Remote(
                command_executor=command_executor,
                options=desired_capabilities)
        except Exception as e:
            print("Error: Fail on starting WebDriver. {}".format(str(e)))
            print("Retry in 2 seconds.")
            sleep(2)


def go_to(driver, url):
    print("Go to {}".format(url))
    driver.get(url)

def wait_for_element_to_be_visible(driver, locator):
    try:
        e = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((locator[1], locator[0])))
    except Exception as e:
        print("Failed to locate element".format(str(e)))
        pass

def get_element(driver, locator):
    try:
        return driver.find_element(by=locator[1], value=locator[0])
    except BaseException as e:
        raise e


def get_elements(driver, locator):
    try:
        return driver.find_elements(by=locator[1], value=locator[0])
    except BaseException as e:
        raise e


def click(driver, locator, idx=None):
    """ Click element """
    if idx:
        # waiting at least one element is ready visible
        # _ = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((locator[1], locator[0]))
        # )
        e = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((locator[1], locator[0])))
        elements = get_elements(driver, locator)
        elements[idx].click()
    else:
        # Get element when it is ready for click
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((locator[1], locator[0]))
        )
        element.click()


def return_text(driver, locator, idx=None):
    """ return element text """
    if idx:
        elements = get_elements(driver, locator)
        return elements[idx].text
    else:
        element = get_element(driver, locator)
        return element.text


def input_text(driver, locator, text, idx=None):
    """ input text into the text field """
    # print("Input text to Page element: {}".format(locator[2]))
    if idx:
        get_elements(driver, locator)[idx].send_keys(text)
    else:
        driver.find_element(by=locator[1], value=locator[0]).send_keys(text)

def click_link_text(driver, text):
    try:
        l = driver.find_element(By.LINK_TEXT, text)
        l.click()
    except BaseException as e:
        raise e




