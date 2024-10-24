import time

import driver
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.description("To verify the error message")
@allure.title("Check if the error message is populating properly")
def test_verifyErrorMessage():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

# Find the Email
    # Rule --> id -->name-->Class name -->Link/Partial(a tag)-->CSS Selector --> XPath
    #< input type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"   //input[@id='login-username']
    # data-qa="hocewoqisi" >
    Email = driver.find_element(By.ID,"login-username")
    Email.send_keys("admin@gmail.com")

# Find the Password
    #< input type = "password"
    # class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe" >
    password=driver.find_element(By.NAME,"password")
    password.send_keys("admin1223")


# Click on Sign In Button
    #< button type = "submit" //button[@name = "submit"]
    # id = "js-login-btn"
    # class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica" >
    signIn_webElement = driver.find_element(By.ID,"js-login-btn")
    signIn_webElement.click()

    # Wait for sometime till the error message appears.
    time. sleep(3)


    # Verify Error message
    #<div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    errorMessage=driver.find_element(By.ID,"js-notification-box-msg")
    print(errorMessage.text)
    assert errorMessage.text == "Your email, password, IP address or location did not match"

