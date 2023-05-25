import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path=r"\Users\city7\OneDrive\Desktop\FINAL\yogastudio\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:9000/login")

# Locate the username and password fields and input the credentials
username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("anju@gmail.com")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("anju123")

driver.get("http://127.0.0.1:9000/appointment/booknow")

# Locate the username and password fields and input the credentials
date_field = driver.find_element(By.NAME, "date")
date_field.send_keys("12-05-2023")

dept_field = driver.find_element(By.NAME, "dep")
dept_field.send_keys("cardiology")

doclist_field = driver.find_element(By.NAME, "doclist")
doclist_field.send_keys("Sebastian")

time_field = driver.find_element(By.NAME, "time")
time_field.send_keys("09:00 - 09:30 AM")

# Submit the login form
time_field.send_keys(Keys.RETURN)

# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, '/html/body/div/div/div/center/div/div[2]/a/button')
if dashboard_element:
    print("Booked successful!")
else:
    print("Booking failed.")


# Close the browser
driver.quit()