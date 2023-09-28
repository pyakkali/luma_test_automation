# prop.py
# lists static test properties, such as selenium/appium desired_capabilities

import sys
from selenium import webdriver


# Set propmodule to enable changing via cmd
propmodule = sys.modules[__name__]

# Browser desired_capabilities
support_browser = {
    'chrome': webdriver.ChromeOptions()
}

# Default Target Browser
browser = "chrome"

# Selenium host
webdriver_url = 'http://127.0.0.1:4444/wd/hub'


# Update variable base on cmd
def set_module_value(key, value):
    setattr(propmodule, key, value)

