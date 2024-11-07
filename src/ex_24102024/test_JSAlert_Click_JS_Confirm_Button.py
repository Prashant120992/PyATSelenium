import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_alert_click_JSConfirm():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(5)
    click_for_JS_confirm=driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    click_for_JS_confirm.click()

    # Wait for alert pop-up to be populated.
    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert=driver.switch_to.alert # To accept an alert.
    alert.dismiss()

    message=driver.find_element(By.XPATH,"//p[@id='result']").text

    assert message == "You clicked: Cancel"

    time.sleep(5)