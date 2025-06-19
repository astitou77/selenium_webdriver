# test_20s.py
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

import logging
import os

import zframework

# define Logging configuration
# Shared directory where logs and screenshots will be saved (e.g., mounted drive or shared folder)
LOG_DIR = '~/Desktop/test_logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'test_run.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# start the test run
logging.info("Starting test run...")

options = ChromeOptions()

# options.set_capability("browserName", "chrome")
# options.set_capability("browserVersion", "137.0.7151.69")
# options.set_capability("platformName", "WINDOWS")
# options.add_argument("--headless")  # Uncomment to run in headless mode

# Connect to the Selenium Grid Hub
driver = webdriver.Remote(
    command_executor='http://192.168.1.11:4444/wd/hub',
    options=options # desired_capabilities=capabilities
)

try:
    # driver = webdriver.Chrome()
    driver.get("https://google.com")
    print("Test started, waiting for 40 seconds...")
    # Wait for 20 seconds
    time.sleep(20)
    print("Test completed, closing the browser.")

    # driver.get("https://www.python.org")
    # assert "Python" in driver.title
    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys("documentation")
    # search_box.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
finally:
    driver.quit()
