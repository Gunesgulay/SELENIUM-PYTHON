# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants as c
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddproducttocardcontroller():
  def setup_method(self, method):
    chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")
    self.driver = webdriver.Chrome(service=chrome_driver_path)
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addproducttocardcontroller(self):
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link")))
    self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
    self.driver.close()
  
