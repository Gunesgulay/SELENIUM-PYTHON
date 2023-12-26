from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 


chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://www.google.com")
driver.maximize_window()   
sleep(5)

input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
sleep(2)

searchButton = driver.find_element(By.NAME,"btnK")
searchButton.click()
sleep(2)

firstResult = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
firstResult.click()
sleep(5)

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
testResult = len(listOfCourses) == 6 
print(f"Test RESULT: {testResult}") 

