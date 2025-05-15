from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

# ChromeDriver path (Make sure the path is correct)
chromedriver_path = "D:\\python project\\chromedriver-win64\\chromedriver.exe"

def get_price(url):
    # Setup Chrome options
    options = Options()
    options.add_argument("--headless")  # Run headless for background processing

    # Specify the path to ChromeDriver using the Service object
    service = Service(executable_path=chromedriver_path)
    
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)

    try:
        # Wait for the price element to load dynamically (10 seconds max)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )

        # Get the page source after the price has loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Extract the price using BeautifulSoup
        price_tag = soup.find("span", {"class": "a-price-whole"})
        if price_tag:
            price_str = re.sub(r"[₹,]", "", price_tag.text.strip())  # Clean the price string
            return float(price_str)  # Return the price as a float
        else:
            print("Price tag not found!")
            return 0.0

    except Exception as e:
        print(f"Error fetching price for {url}: {e}")
        driver.quit()
        return 0.0


