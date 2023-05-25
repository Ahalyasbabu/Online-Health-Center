import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path=r"\Users\city7\OneDrive\Desktop\FINAL\yogastudio\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:9000/cadmin")

# Locate the username and password fields and input the credentials
username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("admin")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin")
time.sleep(5)

driver.get("http://localhost:9000/cadmin")

driver.get("http://localhost:9000/cadmin/doctors")
time.sleep(5)
# Locate the username and password fields and input the credentials
fname_field = driver.find_element(By.NAME, "fname")
fname_field.send_keys("Anila")

lname_field = driver.find_element(By.NAME, "lname")
lname_field.send_keys("Varghese")

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("anila@gmail.com")

qualification_field = driver.find_element(By.NAME, "qualification")
qualification_field.send_keys("MBBS")

experience_field = driver.find_element(By.NAME, "experience")
experience_field.send_keys("5")

dep_field = driver.find_element(By.NAME, "dep")
dep_field.send_keys("Cardiology")


# Submit the login form
dep_field.send_keys(Keys.RETURN)

# Wait for the page to load and check for the presence of the dashboard element
dashboard_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[3]/button[2]')
if dashboard_element:
    print("Successfully added doctor!")
else:
    print("Failed to add doctor.")


# Close the browser
driver.quit()