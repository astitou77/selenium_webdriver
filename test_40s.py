# test_40s.py
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = ChromeOptions()

options.set_capability("browserName", "chrome")
options.set_capability("browserVersion", "137.0.7151.69")
options.set_capability("platformName", "WINDOWS")
# options.set_capability("se:name", "My Parallel Test")
# options.set_capability("se:timeZone", "America/Toronto")

# Connect to the Selenium Grid Hub
driver = webdriver.Remote(
    command_executor='http://192.168.1.11:4444/wd/hub',
    options=options # desired_capabilities=capabilities
)

try:
    # driver = webdriver.Chrome()
    driver.get("https://rumble.com")
    print("Test started, waiting for 40 seconds...")
    # Wait for 40 seconds
    time.sleep(30)
    print("Test completed, closing the browser.")
finally:
    driver.quit()