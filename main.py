import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set path for Selenium Chrome driver
os.environ['PATH'] += r"C:/SeleniumDrivers"

# Initialize new Chrome driver instance
driver = webdriver.Chrome()

# Open Cookie Clicker game website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait until the language selection element (English) is visible
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Find the English language selection button and click it
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait until big cookie element is visible on the page
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Find the big cookie element for clicking
cookie = driver.find_element(By.ID, "bigCookie")

# Main while loop is used to constantly click the big cookie and check for upgrades
while True:
    # Click cookie
    cookie.click()
    
    # Get current number of cookies by extracting text from the cookies counter element
    cookie_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))  # Convert the cookies count to an int
    
    # Check the 4 available products to see if any can be purchased
    for i in range(4):
        # Find the cookie price of the product
        product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(",", "")
        
        # Skip product if price is not a number
        if not product_price.isdigit():
            continue
        
        # Convert product price to int
        product_price = int(product_price)
        
        # If enough cookies are available to buy the product, click the product to purchase it
        if cookie_count >= product_price:
            product = driver.find_element(By.ID, "product" + str(i))
            product.click()
            break  # Exit loop after purchasing an upgrade
