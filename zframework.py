import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def create_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    elif browser_name == "edge":
        options = EdgeOptions()
    else:
        raise Exception("Unsupported browser!")

    options.set_capability("platformName", "WINDOWS")
    return webdriver.Remote(
        command_executor="http://192.168.1.11:4444/wd/hub",
        options=options
    )
