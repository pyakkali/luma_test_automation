import sys
sys.path.append('core')
import os
import prop

def pytest_sessionstart(session):
    pass


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', help='Test Browser')
    parser.addoption('--selenium_host', action='store', help='Selenium Host')


def pytest_configure(config):

    if config.getoption('browser'):
        test_browser = config.getoption('browser')
        prop.set_module_value('browser', test_browser)
        print("Selenium Browser is {}".format(test_browser))

    if config.getoption('selenium_host'):
        selenium_host = config.getoption('selenium_host')
        prop.set_module_value('selenium_host', selenium_host)
        print("Selenium Host is {}".format(selenium_host))
