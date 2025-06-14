# import sys
# Use  pip show pip to find site-packages path
# sys.path.append('/Users/adnane/Desktop/selenium_webdriver/.venv/lib/python3.13/site-packages')  
# import selenium_webdriver


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
# from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(f"Page title is: {title}")
# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "my-text"))
)
# Alternatively, you can use implicit wait
#
# driver.implicitly_wait(10)  # seconds
# Set implicit wait to 0.5 seconds
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

