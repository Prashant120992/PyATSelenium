import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest


@allure.title("Verify titles of the search are getting populated.")
@allure.description("Populate the Product name and their prices side by side separated by ||")

def test_ebay_Product_list_with_Price():
    symbol = "||"
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    time.sleep(2)
    search_bar = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_bar.send_keys("Macmini")
    time.sleep(5)
    search= driver.find_element(By.CSS_SELECTOR, "#gh-btn")
    search.click()
    time.sleep(5)
    titles = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
    prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

    # for title in output_titles:
    #     print(title.text)
    # assert len(output_titles) == 62
    #
    # # Loop through each web element
    # for price in output_prices:
    #     print(price.text)

    for title, price in zip(titles,prices):

        title_text = title.text.strip()
        price_text = price.text.strip()

        # Print the title and price side by side
        print(f"Title: {title_text} Symbol:{symbol} Price: {price_text}")