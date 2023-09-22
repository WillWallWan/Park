import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


def park():
    service = Service(executable_path=r'C:\Users\willy\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    
    # Initialize a wait object with a timeout of 10 seconds
    wait = WebDriverWait(driver, 10)


    driver.get('https://my.nyc.flowbirdapp.com/#/Parking?panel=login')

    

    try:
        # Using waits before finding elements to ensure that they are loaded and interactable
        username_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and @size="20"]')))
        username_field.send_keys("willy-wan@hotmail.com")
        
        # Finding the password field and sending the password
        password_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password" and @size="20"]')))
        password_field.send_keys("Iluvrobin123321")
        
        # Finding the login button and clicking it
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login--button")))
        login_button.click()
        
        print("Logged in successfully")
    except Exception as e:
        print("Error during login:", str(e))

    time.sleep(1)

    zone_code = "413870"

    zone_input_xpath = '//input[@type="text" and @size="20"]'
    zone_input = wait.until(EC.element_to_be_clickable((By.XPATH, zone_input_xpath)))
    zone_input.send_keys(zone_code)

    start_parking_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button-primary.margin-bottom-10-important')))
    start_parking_button.click()

    end_time_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.w-output--container')))
    end_time_button.click()

    input_end_time = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='To']/preceding-sibling::input")))

    input_end_time.click()

    time.sleep(1)

    try:
        # Locate the hours column
        hours_column = driver.find_element(By.XPATH, "//div[@class='dwwl dwwl3']")

        # Initialize ActionChains
        actions = ActionChains(driver)

        # Move to the hours column and perform a drag (scroll) action
        actions.move_to_element(hours_column).click_and_hold().move_by_offset(0, -100).release().perform()


        print("Scrolled down in the hours section")
    except Exception as e:
        print("Error during the operation:", str(e))


    # Locate the confirm button
    confirm_button = driver.find_element(By.XPATH, "//div[@class='dwb1 dwb-e dwb']")

    # Click the confirm button
    confirm_button.click()

    process_to_payment_button = driver.find_element(By.XPATH, "//button/span[text()=' Process to payment ']")

    # Click the 'Process to payment' button
    process_to_payment_button.click()

    # Locate the 'Purchase' button using the text inside it
    purchase_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button-primary')][.//span[contains(text(), 'Purchase')]]")))

    # Click the 'Purchase' button
    purchase_button.click()

    print("Purchase button clicked")



    
    # Adding a delay before closing the driver
    time.sleep(5)

    driver.close()


park()
