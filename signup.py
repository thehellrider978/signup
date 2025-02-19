from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Your invitation code
INVITATION_CODE = "223454413643"

# Generate a random mobile number (10-digit Indian number)
def generate_random_mobile():
    return "9" + "".join(str(random.randint(0, 9)) for _ in range(9))

# Configure WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (optional)
driver = webdriver.Chrome(options=chrome_options)

# Open registration page
driver.get("https://www.in111.in/#/register")
time.sleep(2)  # Wait for the page to load

# Automate 1000 registrations as an example (adjust as needed)
for i in range(1000):
    try:
        mobile_number = generate_random_mobile()
        
        # Locate input fields and enter data
        driver.find_element(By.NAME, "phone").send_keys(mobile_number)  # Adjust selector if needed
        driver.find_element(By.NAME, "inviteCode").send_keys(INVITATION_CODE)  # Adjust selector if needed
        driver.find_element(By.NAME, "password").send_keys("Test@1234")  # Use a default password
        driver.find_element(By.NAME, "confirmPassword").send_keys("Test@1234")
        
        # Submit the form
        driver.find_element(By.CLASS_NAME, "submit-btn").click()  # Adjust selector if needed
        time.sleep(3)  # Wait for response
        
        print(f"Registration {i+1} successful with mobile: {mobile_number}")
    except Exception as e:
        print(f"Error in registration {i+1}: {e}")

# Close browser
driver.quit()
