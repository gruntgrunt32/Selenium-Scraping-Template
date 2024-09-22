from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle
import time
import random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# How to use the selenium template
# 1. Run python -m venv venv
# 2. pip install -r requirements.txt
# 3. Change the USER_DATA_DIRECTORY and YOUR_USER_AGENT variables
# 4. Use the functions below to interact with the browser
# 5. Run the script


# get element by xpath
# driver.find_element(By.XPATH, xpath)


# get element by class name
# driver.find_element(By.CLASS_NAME, class_name)


# get element by id
# driver.find_element(By.ID, id)


# switch to iframe
# driver.switch_to.frame(iframe)


# switch to default content
# driver.switch_to.default_content()

# get the user data directory by running chrome://version/ in the browser and change the path accordingly
USER_DATA_DIRECTORY = "YOUR_USER_DATA_DIRECTORY"

# how to get user agent: https://www.whatismybrowser.com/detect/what-is-my-user-agent
YOUR_USER_AGENT = "YOUR_USER"

def save_cookies(driver):
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

def load_cookies(driver):
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
    except:
        pass

def browser_init():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=" + YOUR_USER_AGENT)
    chrome_options.add_argument("--user-data-dir=" + USER_DATA_DIRECTORY)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('https://www.google.com/')
    load_cookies(driver)
    return driver


def random_sleep():
    time.sleep(random.randint(1, 4))

def wait_for_element(driver, xpath, timeout=30):
    start_time = time.time()
    while True:
        try:
            element = driver.find_element(By.XPATH, xpath)
            return element
        except:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > timeout:
                print(f"Timeout reached after {timeout} seconds")
                break
            pass
        

if __name__ == "__main__":
    driver = browser_init()
    



