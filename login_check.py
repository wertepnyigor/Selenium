import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def skip_engine_check():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    return chrome_options

def create_driver(website_address):
    chrome_driver = webdriver.Chrome(options=search_engine)
    chrome_driver.maximize_window()
    chrome_driver.get(website_address)
    WebDriverWait(chrome_driver, 5).until(
        EC.presence_of_element_located((By.ID, "searchbox_input"))
    )

    return chrome_driver

def login(login, password):
    username_field = driver.find_element(By.ID, "wpName1")
    username_field.clear()
    username_field.send_keys(login)

    password_field = driver.find_element(By.ID, "wpPassword1")
    password_field.clear()
    password_field.send_keys(password)

    button = driver.find_element(By.ID, "wpLoginAttempt")
    button.submit()


try:
    search_engine = skip_engine_check()
    website = "https://duckduckgo.com"
    driver = create_driver(website)

    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.clear()
    search_box.send_keys("python wiki" + Keys.RETURN)

    result = driver.find_element(By.PARTIAL_LINK_TEXT, "Python")
    result.click()

    login_button = driver.find_element(By.ID, "pt-login-2")
    login_button.click()

    login("user1", "password1")

    if driver.find_element(By.CLASS_NAME, "cdx-message__icon").is_displayed():
        print("PASS - cannot login with those credetnials")
    else:
        print("FAIL")

    time.sleep(5)

except:
    raise ModuleNotFoundError

finally:

    driver.close()