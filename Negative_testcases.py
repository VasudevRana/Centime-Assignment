import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_01_existing_user_registered(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("frt456@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
        time.sleep(1)
        #click on to register button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify Login successful
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "User already registered ,Please Login")
        time.sleep(2)

    def test_02_register_password_blank(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("frt456@gmail.com")
        time.sleep(1)
        #click on to register button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify Login successful
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "Password Blank ,Please fill")
        time.sleep(1)

    def test_03_register_username_blank(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").click()
        self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
        time.sleep(1)
        # click on to register button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify Login successful
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "Username field blank")
        time.sleep(1)

    def test_04_register_username_and_password_blank(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").click()
        self.driver.find_element(By.ID, "reg_password").click()
        time.sleep(1)
        # click on to register button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify Login successful
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "Username field blank")
        time.sleep(1)

    def test_05_login_user_not_registered(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "username").send_keys("446546465@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Q@3#")
        self.driver.find_element(By.ID, "password").send_keys("QweQrt")
        self.driver.find_element(By.ID, "password").send_keys("Qyuu")
        self.driver.find_element(By.ID, "password").send_keys("QiiQ12")
        # Click on login button
        Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        Login_submit_button.click()
        time.sleep(2)
        # Verify Login successful
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "User not registered")
        time.sleep(2)

    def test_06_login_password_blank(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "username").send_keys("45@gmail.com")
        Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        Login_submit_button.click()
        time.sleep(1)
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "password Blank")
        time.sleep(2)

    def test_07_login_username_blank(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "password").send_keys("vishal.rana@12()")
        Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        Login_submit_button.click()
        time.sleep(3)
        error_message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Error:']")
        self.assertTrue(error_message.text == 'Error:')
        print(error_message.text, "Username Blank")
        time.sleep(4)

    def test_08_update_the_value_to_zero(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button.click()
        self.driver.get("https://practice.automationtesting.in/basket/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@title='Qty']").clear()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Update Basket']"))
                                         ).click()
        time.sleep(1)
        upd_message = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-message']")
        time.sleep(1)
        if 'updated.' in upd_message.text:
            print("Update item , Basket is Empty")
        else:
            print("not Updated item")
        time.sleep(5)

    def test_09_more_than_one_item_from_cart(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button_2 = self.driver.find_element(By.XPATH, "//a[@data-product_id='160']")
        time.sleep(1)
        add_to_cart_button_2.click()
        time.sleep(1)
        self.driver.get("https://practice.automationtesting.in/basket/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        time.sleep(1)
        del_message = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-message']")
        time.sleep(1)
        if 'removed.' in del_message.text:
            print("removed item")
        else:
            print("not removed item")
        time.sleep(5)

    def test_10_when_single_item_present_in_cart(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(2)
        self.driver.get("https://practice.automationtesting.in/basket/")
        time.sleep(1)
        # Delete the product
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        time.sleep(1)
        del_message = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-message']")
        time.sleep(1)
        if 'removed.' in del_message.text:
            print("removed item")
        else:
            print("not removed item")

    def test_11_when_item_not_present_in_cart(self):
        # when there is a text as empty basket:
        self.driver.get("https://practice.automationtesting.in/basket/")
        time.sleep(2)
        empty_text = self.driver.find_element(By.XPATH, "//p[@class='cart-empty']")
        assert empty_text.text == 'Your basket is currently empty.'
        self.driver.find_element(By.XPATH, "//a[@class='button wc-backward']").click()
        time.sleep(2)
    
    def test_12_user_registered_billing_address_blank(self):
        ##############3ENTER NEW Email everytime for rgestering###########################
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("new_user_1015611@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
        time.sleep(1)
        # Click on registration button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify register successfful

        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(1)

        # Billing adress:
        self.driver.find_element(By.XPATH, "//a[@class='edit']").click()
        time.sleep(1)

        shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        shop_button.click()
        time.sleep(2)
        del_message = self.driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']")
        time.sleep(1)
        if 'required field.' in del_message.text:
            print("removed item")
        else:
            print("not removed item")

    def test_13_new_user_registered_add_shipping_address(self):
            self.driver.get('https://practice.automationtesting.in/my-account/')
            self.driver.find_element(By.ID, "reg_email").send_keys("new_shiipping0098_user123@gmail.com")
            time.sleep(3)
            self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
            time.sleep(3)
            # Click on registration button
            registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
            registration_submit_button.click()
            time.sleep(3)
            # Verify register successfful

            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)

            # Shipping adress:
            self.driver.find_element(By.XPATH, "//a[contains(@href,'shipping')]").click()
            time.sleep(3)

            shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
            shop_button.click()
            time.sleep(2)
            check_message = self.driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']")
            time.sleep(1)
            if 'required field.' in check_message.text:
                print("removed item")
            else:
                print("not removed item")

    def tearDown(self):
        self.driver.quit()


if __name__ == "_main_":
    unittest.main()