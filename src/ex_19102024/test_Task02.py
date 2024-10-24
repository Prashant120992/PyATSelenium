import time

import driver
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.description("To verify the error message")
@allure.title("Check if the error message is populating properly")
def test_verify_OpenCart_Message_OpenCart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(2)

    firstNameWeb_Element = driver.find_element(By.ID,"input-firstname")
    firstNameWeb_Element.send_keys("Prashant")
    time.sleep(2)

    lastNameWeb_Element = driver.find_element(By.NAME, "lastname")
    lastNameWeb_Element.send_keys("H")
    time.sleep(2)

    Email_Web_Element = driver.find_element(By.ID, "input-email")
    Email_Web_Element.send_keys("prashant1@gmail.com")
    time.sleep(2)

    phone_Web_Element = driver.find_element(By.ID, "input-telephone")
    phone_Web_Element.send_keys("99999999999")
    time.sleep(2)

    password_Web_Element = driver.find_element(By.ID, "input-password")
    password_Web_Element.send_keys("admin123")
    time.sleep(2)

    confirm_password_Web_Element = driver.find_element(By.ID, "input-confirm")
    confirm_password_Web_Element.send_keys("admin123")
    time.sleep(3)


    privacy_Web_Element = driver.find_element(By.XPATH, "//input[@name='agree']")
    privacy_Web_Element.click()
    time.sleep(2)

    submit_Web_Element = driver.find_element(By.XPATH, "//input[@value='Continue']")
    submit_Web_Element.click()

    time. sleep(3)

    created_Message=driver.find_element(By.ID,"content")
    time.sleep(3)
    print(created_Message.text)
    assert created_Message == "Your Account Has Been Created!"

