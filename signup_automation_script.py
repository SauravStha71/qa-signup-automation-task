from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# --- Setup driver (auto installs chromedriver) ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://authorized-partner.netlify.app/login")
wait = WebDriverWait(driver, 10)

# --- Step 1: Click "Sign Up" ---
signup_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
signup_button.click()

# --- Step 2: Fill first signup form ---
first_name = "John"
last_name = "Doe"
email = f"test{random.randint(1000,9999)}@example.com"
password = "Test@12345"

wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
driver.find_element(By.NAME, "lastName").send_keys(last_name)
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

# --- Step 3: Fill second signup form ---
wait.until(EC.visibility_of_element_located((By.NAME, "companyName"))).send_keys("Test Company")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

# --- Step 4: Fill final signup form ---
wait.until(EC.visibility_of_element_located((By.NAME, "address"))).send_keys("123 Test Street")
driver.find_element(By.NAME, "city").send_keys("Kathmandu")
driver.find_element(By.NAME, "zip").send_keys("44600")
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

print("✅ Signup automation completed successfully!")

time.sleep(5)
driver.quit()
