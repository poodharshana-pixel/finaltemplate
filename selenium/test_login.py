
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

page = Path("login.html").resolve().as_uri()
driver = webdriver.Chrome()

try:
    driver.get(page)

    print("Chrome opened!")
    print("Enter the username and password MANUALLY.")
    print("Click the Login button in the browser.")

    # Wait while you interact with the browser
    input("After clicking Login, return here and press Enter...")

    username = driver.find_element(By.ID, "username").get_attribute("value")
    password = driver.find_element(By.ID, "password").get_attribute("value")
    message = driver.find_element(By.ID, "loginMessage").text

    if username == "admin" and password == "12345":
        expected = "Login successful"
    else:
        expected = "Invalid credentials"

    print("\nExpected:", expected)
    print("Actual:  ", message)

    if message == expected:
        print("TEST PASSED")
    else:
        print("TEST FAILED")

    input("\nPress Enter to close Chrome...")

finally:
    driver.quit()
