"""Selenium WebDriver demo: browser opens, user types manually, script verifies result."""
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

page = (Path(__file__).parent / "selenium_demo.html").resolve().as_uri()
driver = webdriver.Chrome()
try:
    driver.get(page)
    print("Enter admin / 12345 (or test invalid credentials) in the browser.")
    input("After clicking Login, return here and press Enter to verify: ")
    username = driver.find_element(By.ID, "username").get_attribute("value")
    password = driver.find_element(By.ID, "password").get_attribute("value")
    actual = driver.find_element(By.ID, "message").text
    expected = "Login successful" if username == "admin" and password == "12345" else "Invalid credentials"
    print("Expected:", expected, "| Actual:", actual)
    print("TEST PASSED" if actual == expected else "TEST FAILED")
    input("Press Enter to close Chrome...")
finally:
    driver.quit()
