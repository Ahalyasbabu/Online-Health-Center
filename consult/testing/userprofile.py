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

driver.get("http://127.0.0.1:9000/profile")

# Locate the username and password fields and input the credentials
fname_field = driver.find_element(By.NAME, "fname")
fname_field.send_keys("Anju")

lname_field = driver.find_element(By.NAME, "lname")
lname_field.send_keys("John")


# Submit the login form
lname_field.send_keys(Keys.RETURN)

# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
if dashboard_element:
    print("Profile updated successful!")
else:
    print("Profile updation failed.")


# Close the browser
driver.quit()