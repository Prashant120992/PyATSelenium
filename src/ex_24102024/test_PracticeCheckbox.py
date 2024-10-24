import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.description("Verify Checkbox.")
def test_verify_check_box():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_name_element = driver.find_element(By.XPATH, "//input[@name = 'firstname']")
    first_name_element.send_keys("Prashant")

    last_name_element = driver.find_element(By.XPATH, "//input[@name = 'lastname']")
    last_name_element.send_keys("H")

    gender_element = driver.find_element(By.XPATH, "//input[@value= 'Male']")
    gender_element.click()
    time.sleep(2)
    years_of_experience_element=driver.find_element(By.XPATH,"//input[@value= '3']")
    years_of_experience_element.click()
    time.sleep(2)
    profession_element = driver.find_element(By.XPATH,"//input[@value= 'Automation Tester']")
    profession_element.click()
    time.sleep(2)
    automation_tools_element= driver.find_element(By.XPATH,"//input[@value= 'Selenium Webdriver']")
    automation_tools_element.click()

