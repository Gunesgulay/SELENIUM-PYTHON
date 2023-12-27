from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

class Test_Sauceclass:
    def setup_method(self):
        chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()  

    @pytest.mark.skip
    def test_two_fields_empty(self):
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username", [("standard_user")])
    def test_one_fields_empty(self, username):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce")])    
    def test_invalid_login(self, username, password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])    
    def test_product_count(self, username, password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        listOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item_label")
        assert len(listOfProducts) == 6 

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])    
    def test_add_product_to_cart(self, username, password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()

        goToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".shopping_cart_link")))
        goToCart.click()

        productName = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name")
        assert productName.text == "Sauce Labs Backpack"

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])    
    def test_checkout_all_fields_empty(self, username, password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()

        goToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".shopping_cart_link")))
        goToCart.click()

        checkoutButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutButton.click()

        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()

        errorMessageController = self.driver.find_element(By.CSS_SELECTOR,"h3")
        assert errorMessageController.text == "Error: First Name is required"

    @pytest.mark.parametrize("username, password, firstname, lastname, zipcode", [("standard_user", "secret_sauce", "test", "automation", "12345")])    
    def test_successful_purchase(self, username, password, firstname, lastname, zipcode):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()

        goToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".shopping_cart_link")))
        goToCart.click()   

        checkoutButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutButton.click() 

        enterFirstName = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        enterFirstName.send_keys(firstname)

        enterLastName = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        enterLastName.send_keys(lastname)

        enterZipCode = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        enterZipCode.send_keys(zipcode)

        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()

        finishButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"finish")))
        finishButton.click()

        messageController = self.driver.find_element(By.CSS_SELECTOR,".complete-header")
        assert messageController.text == "Thank you for your order!"