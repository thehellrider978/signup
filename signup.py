import time
import random
import cv2
import numpy as np
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

# Function to capture CAPTCHA image from the webpage
def capture_captcha(driver, captcha_element):
    location = captcha_element.location
    size = captcha_element.size
    driver.save_screenshot("screenshot.png")
    
    image = Image.open("screenshot.png")
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    
    captcha_image = image.crop((left, top, right, bottom))
    captcha_image.save("captcha.png")
    return "captcha.png"

# Function to solve text-based CAPTCHA using OCR (Tesseract)
def solve_text_captcha(image_path):
    image = Image.open(image_path)
    captcha_text = pytesseract.image_to_string(image).strip()
    return captcha_text

# Function to solve slider CAPTCHA using OpenCV
def solve_slider_captcha(background_path, puzzle_piece_path):
    bg_img = cv2.imread(background_path, 0)
    piece_img = cv2.imread(puzzle_piece_path, 0)
    
    result = cv2.matchTemplate(bg_img, piece_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    
    return max_loc[0]  # Return the x-coordinate where the slider should be moved

# Function to simulate human-like typing
def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.4))  # Simulate natural typing speed

# Setup Firefox options
options = Options()
options.headless = False  # Set to True for background execution

# Start the Firefox WebDriver
driver = webdriver.Firefox(options=options)

# Open the registration page
driver.get("https://www.in111.in/#/register")
time.sleep(3)

# Fill in the registration details
phone_number = f"9{random.randint(100000000, 999999999)}"  # Generate a random phone number
invitation_code = "223454413643"

# Find and fill phone number field
phone_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/div/div/div[1]/div[2]/input')
human_typing(phone_input, phone_number)

# Find and fill invitation code field
invitation_input = driver.find_element(By.NAME, "invitationCode")
human_typing(invitation_input, invitation_code)

# Solve CAPTCHA
try:
    # Locate the CAPTCHA element (Update the XPath according to the site)
    captcha_element = driver.find_element(By.XPATH, '//*[@id="captcha-element"]')
    captcha_path = capture_captcha(driver, captcha_element)

    # Solve using OCR
    captcha_text = solve_text_captcha(captcha_path)
    
    # Enter the solved CAPTCHA text
    captcha_input = driver.find_element(By.NAME, "captcha")
    human_typing(captcha_input, captcha_text)
    print(f"Solved CAPTCHA: {captcha_text}")

except Exception as e:
    print("Error solving CAPTCHA:", str(e))

# Simulate human-like mouse movement
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
action = ActionChains(driver)
for _ in range(5):
    action.move_by_offset(random.randint(5, 10), random.randint(5, 10)).perform()
    time.sleep(random.uniform(0.2, 0.5))

# Click the submit button
submit_button.click()
time.sleep(5)

# Close the browser
driver.quit()
