from selenium import webdriver
import allure


@allure.title("Verify the Title of the page")
def test_sample():
     driver = webdriver.Chrome()
     driver.get("https://katalon-demo-cura.herokuapp.com/")
     print(driver.title)
     assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
     assert driver.title == "CURA Healthcare Service"
     assert driver.page_source.__contains__("CURA Healthcare Service")