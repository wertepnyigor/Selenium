from login_check import create_driver

def test_create_driver(create_driver):
    create_driver.get("https://duckduckgo.com")
    assert create_driver.title == "Duck"

