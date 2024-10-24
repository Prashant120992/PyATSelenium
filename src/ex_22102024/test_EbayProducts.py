from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verify_EbayProduct():
    symbol = "||"
#Replace 'your_chromedriver_path' with the actual path to your ChromeDriver
    driver = webdriver.Chrome()
    driver.get('https://www.ebay.com/')

# Wait for the search bar to be clickable (adjust wait time if needed)
    search_bar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gh-ac')))

# Enter a search term (replace with your desired search)
    search_bar.send_keys('macbook')

# Submit the search form
    search_button = driver.find_element(By.CSS_SELECTOR, '#gh-btn')
    search_button.click()

# Wait for the search results to load (adjust wait time if needed)
    product_listings = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.s-item')))

# Extract product details
    for listing in product_listings:

        # Extract product name (adjust selectors based on actual structure)
            product_name = listing.find_element(
            By.CSS_SELECTOR, '.s-item__title')
            product_name=product_name.text.strip()

        # Extract product price (adjust selectors based on actual structure)
            product_price = listing.find_element(
            By.CSS_SELECTOR, '.s-item__price')
            product_price = product_price.text.strip()


            print(f"Product Name: {product_name} Symbol:{symbol} Price: {product_price}")


