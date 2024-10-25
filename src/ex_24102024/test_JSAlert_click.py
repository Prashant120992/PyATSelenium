import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_alert1_click():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(5)
    click_for_JS_alert_button=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    click_for_JS_alert_button.click()

    # Wait for alert pop-up to be populated.
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert=driver.switch_to.alert # To accept an alert.
    alert.accept()

    message=driver.find_element(By.ID,"result").text

    assert message == "You successfully clicked an alert"

    time.sleep(5)