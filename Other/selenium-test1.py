# This code snippet demonstrates how to use Selenium WebDriver to automate a web form submission.
# It opens a web page, fills out a text box, submits the form, and verifies the result.
# The script uses the Chrome WebDriver to interact with the web page.
# Make sure to have the Chrome WebDriver installed and available in your PATH.

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Print the title of the page
title = driver.title
print(f"Page title is: {title}")

# Wait for the page to load completely
driver.implicitly_wait(10)  # seconds

# Alternatively, you can use explicit wait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "my-text"))
# )

# Find the text box and submit button
text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

# Fill out the text box and submit the form
text_box.send_keys("Selenium")
submit_button.click()
#
# Verify the result
result = driver.find_element(By.ID, "message")
assert result.text == "Received! Thanks for your submission.", "Submission failed!"
# Close the browser
driver.quit()




