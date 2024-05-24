from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Use webdriver_manager to automatically manage WebDriver
service = Service(GeckoDriverManager().install())

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=service)

# Open the desired URL
url = 'https://www.example.com'
driver.get(url)

# Optional: Wait for a few seconds to see the result
import time
time.sleep(5)
class FindElement:
    def Details(self):
        driver=Webriver.get("Google.com")
        driver.get("")

# Close the browser
driver.quit()
