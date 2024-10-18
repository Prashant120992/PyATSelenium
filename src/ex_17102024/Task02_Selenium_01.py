import time

import driver
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


def test_katalon_demo_Task01():
    driver = webdriver.Chrome() # Creation of a session
    driver.get("https://katalon-demo-cura.herokuapp.com/") #Navigate to URL
    driver.maximize_window()
    time.sleep(2)
    # Locator of make appointment
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    # Assigning wait for 2 Secs
    time.sleep(2)
    # Clicking Make appointment button
    make_appointment.click()

    # Verify the Current URL
    verify=driver.current_url
    assert verify == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    # Login
    user_name = driver.find_element(By.ID, "txt-username")
    user_name.send_keys("John Doe")

    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    Login=driver.find_element(By.ID, "btn-login")
    Login.click()
    current_url1 = driver.current_url
    assert current_url1 == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)