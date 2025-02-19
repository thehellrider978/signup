from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Your invitation code
INVITATION_CODE = "223454413643"

# Generate a random mobile number (10-digit Indian number)
def generate_random_mobile():
    return "9" + "".join(str(random.randint(0, 9)) for _ in range(9))

# Configure WebDriver for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--log-level=3")  # Suppress logs

driver = webdriver.Chrome(options=chrome_options)

# Open registration page
driver.get("https://www.in111.in/#/register")
time.sleep(2)  # Wait for the page to load

# Automate multiple registrations
for i in range(1000):  # Adjust the number as needed
    try:
        mobile_number = generate_random_mobile()
        
        # Locate input fields and enter data (Adjust selectors as per website)
        driver.find_element(By.NAME, "phone").send_keys(mobile_number)
        driver.find_element(By.NAME, "inviteCode").send_keys(INVITATION_CODE)
        driver.find_element(By.NAME, "password").send_keys("Test@1234")
        driver.find_element(By.NAME, "confirmPassword").send_keys("Test@1234")
        
        # Submit the form
        driver.find_element(By.CLASS_NAME, "submit-btn").click()
        time.sleep(3)  # Wait for response
        
        print(f"Registration {i+1} successful with mobile: {mobile_number}")
    except Exception as e:
        print(f"Error in registration {i+1}: {e}")

# Close browser
driver.quit()
