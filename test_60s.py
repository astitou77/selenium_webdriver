import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

options = ChromeOptions()

options.set_capability("browserName", "chrome")
options.set_capability("browserVersion", "137.0.7151.69")
options.set_capability("platformName", "WINDOWS")
# options.set_capability("se:name", "My Parallel Test")
# options.set_capability("se:timeZone", "America/Toronto")

driver = webdriver.Remote(
    command_executor='http://192.168.1.11:4444/wd/hub',
    options=options  # This replaces `desired_capabilities=capabilities`
)

try:
    driver.get("https://costco.com")
    print("Test started, waiting for 60 seconds...")
    time.sleep(40)
    print("Test completed, closing the browser.")
finally:
    driver.quit()


'''
def create_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    elif browser_name == "edge":
        options = EdgeOptions()
    else:
        raise Exception("Unsupported browser!")

    # options.set_capability("platformName", "WINDOWS")
    return webdriver.Remote(
        command_executor="http://192.168.1.11:4444/wd/hub",
        options=options # desired_capabilities=capabilities
    )



for browser in ["chrome", "firefox", "edge"]:
    driver = create_driver(browser)
    
    # ----- run test... -----
    # ...
    # ----- test ends here -----

    driver.quit()
'''
