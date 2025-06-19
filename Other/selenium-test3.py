import multiprocessing
from selenium import webdriver

def open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    wait_time = 5  # seconds
    driver.implicitly_wait(wait_time)
    # Alternatively, you can use explicit wait
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # WebDriverWait(driver, wait_time).until(EC.title_contains("Google"))
    # Print the title of the page

    print(driver.title)
    driver.quit()

def open_bing():
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    wait_time = 5  # seconds
    driver.implicitly_wait(wait_time)
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=open_google)
    p2 = multiprocessing.Process(target=open_bing)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

