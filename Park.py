import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


def park():
    service = Service(executable_path=r'C:\Users\willy\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    
    # Initialize a wait object with a timeout of 10 seconds
    # wait = WebDriverWait(driver, 10)


    driver.get('https://my.nyc.flowbirdapp.com/#/Parking?panel=login')

    time.sleep(5)

    try:
        # Using waits before finding elements to ensure that they are loaded and interactable
        username_field = wait.until(EC.element_to_be_clickable((By.ID, "w-input--8506283350331578")))
        username_field.send_keys("willy-wan@hotmail.com")
        
        # Finding the password field and sending the password
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "w-input--8861484250143397")))
        password_field.send_keys("Iluvrobin123321")
        
        # Finding the login button and clicking it
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login--button")))
        login_button.click()
        
        print("Logged in successfully")
    except Exception as e:
        print("Error during login:", str(e))

    zone_code = "413279"
    
    zone_input = wait.until(EC.element_to_be_clickable((By.ID, 'w-input--9356375178080452')))
    zone_input.send_keys(zone_code)

    start_parking_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button-primary.margin-bottom-10-important')))
    start_parking_button.click()
    
    # Adding a delay before closing the driver
    time.sleep(5)

    driver.close()


park()
