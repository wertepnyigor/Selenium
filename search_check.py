from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def skip_engine_check():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    return chrome_options

def create_driver(website_address):
    driver = webdriver.Chrome(options=search_engine)
    driver.maximize_window()
    driver.get(website_address)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "searchbox_input"))
    )
    return driver

try:
    search_engine = skip_engine_check()
    driver = create_driver("https://duckduckgo.com")

    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.clear()
    search_box.send_keys("python wiki" + Keys.RETURN)

    result = driver.find_element(By.PARTIAL_LINK_TEXT, "Python")
    result.click()

    # change_language = driver.find_element(By.ID, "p-lang-btn-checkbox")
    # change_language.click()

    if "wiki/Python" in driver.current_url:
        print("PASS")
    else:
        print("FAIL")

    # language = driver.find_element(By.XPATH,"""//*[@id="search"]/div/div/input[2]""")
    # language.click()
    # language.clear()
    # language.send_keys("english" + Keys.RETURN)

    time.sleep(5)

except:
    raise ModuleNotFoundError

finally:
    driver.close()