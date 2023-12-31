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

class TestTwofieldsempty():
  def setup_method(self, method):
    chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")
    self.driver = webdriver.Chrome(service=chrome_driver_path)
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_twofieldsempty(self):
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == "Epic sadface: Username is required"
  