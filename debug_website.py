import subprocess
import sys

def install_packages():
    """Install required packages"""
    packages = ['selenium', 'webdriver-manager']
    for package in packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package} already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Setting up environment...")
install_packages()
print("Environment ready!\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def debug_website():
    """Debug script to see what's actually on the website"""
    print("🔍 DEBUG MODE: Analyzing website structure...")
    
    # Setup browser
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Go to website
        print("🌐 Loading website...")
        driver.get("https://authorized-partner.netlify.app/login")
        time.sleep(5)
        
        print(f"📄 Current URL: {driver.current_url}")
        print(f"📝 Page Title: {driver.title}")
        
        # Check if page loaded
        if "authorized-partner" not in driver.current_url:
            print("❌ Website didn't load properly!")
            return
        
        # Get all links on page
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\n🔗 Found {len(links)} links on page:")
        for link in links:
            text = link.text.strip()
            if text and len(text) < 50:  # Only show reasonable length text
                print(f"   - '{text}'")
        
        # Get all buttons
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"\n🔄 Found {len(buttons)} buttons on page:")
        for button in buttons:
            text = button.text.strip()
            if text and len(text) < 50:
                print(f"   - '{text}'")
        
        # Get all input fields
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"\n📝 Found {len(inputs)} input fields on page:")
        for input_field in inputs:
            input_type = input_field.get_attribute("type") or "text"
            input_name = input_field.get_attribute("name") or "no name"
            input_placeholder = input_field.get_attribute("placeholder") or "no placeholder"
            print(f"   - Type: {input_type}, Name: {input_name}, Placeholder: {input_placeholder}")
        
        # Try to find signup link specifically
        print(f"\n🎯 Looking for signup links specifically...")
        signup_keywords = ["sign up", "register", "create account", "don't have an account"]
        for keyword in signup_keywords:
            try:
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{keyword}')]")
                if elements:
                    print(f"✅ Found element with text: '{keyword}'")
                    for element in elements:
                        print(f"   - Tag: {element.tag_name}, Text: '{element.text}'")
            except:
                pass
        
        print(f"\n📋 Full page text (first 1000 chars):")
        print(driver.page_source[:1000])
        
        # Keep browser open
        print(f"\n⏳ Browser will stay open for 30 seconds...")
        time.sleep(30)
        
    except Exception as e:
        print(f"❌ Error during debugging: {e}")
    finally:
        driver.quit()

# Run the debug script
debug_website()