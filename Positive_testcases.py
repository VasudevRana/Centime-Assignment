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

    def test_01_Complete_flow_register_from_checkout_page_(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1300)")
        #Add two products
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        add_to_cart_button.click()
        time.sleep(2)
        add_to_cart_button_two = self.driver.find_element(By.XPATH, "//a[@data-product_id='160']")
        add_to_cart_button_two.click()
        #View Basket link which was hidden will get active for clicking
        view_basket_link = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, "View Basket")))
        view_basket_link.click()
        time.sleep(2)
        #remove element from the cart
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        # Verify user is redirected to "View Basket" page
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("Hinata")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("Shoyo")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("ssrid")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("kp9df8uion@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("7854120369")
        time.sleep(1)
        #self.driver.find_element(By.XPATH,"//html[1]/body[1]/div[3]").click()
        #self.driver.find_element(By.XPATH, "//div[@id='s2id_autogen1_search']").send_keys("Bahamas")
        #wait_for_name=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='select2-match']")))
        #wait_for_name.click()
        #time.sleep(1)
        # select_country.select_by_visible_text('Canada')
        self.driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("house no 987")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("canada")
        time.sleep(1)
        # select = Select(self.driver.find_element(By.ID, "billing_state"))
        # select.select_by_visible_text('Manitoba')
        self.driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("gfgftdryhfhg")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("110061")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='createaccount']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='account_password']").send_keys("ky@123<>99")
        time.sleep(1)

        place_order_button = self.driver.find_element(By.XPATH, "//input[@id='place_order']")
        place_order_button.click()
        time.sleep(2)
        # verify the addresss is added
        verify_text = self.driver.find_element(By.XPATH, "//p[@class='woocommerce-thankyou-order-received']")
        assert verify_text.text == 'Thank you. Your order has been received.'
        time.sleep(3)

    def test_02_complete_flow_login_from_checkout_page_when_address_data_is_not_present(self):
        ##########PRECONDITION IS USER SHOULD BE REGISTERED BUT THERE ADDRESS SHOULD NOT BE SAVED##############
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(2)
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button_two = self.driver.find_element(By.XPATH, "//a[@data-product_id='160']")
        add_to_cart_button_two.click()
        view_basket_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Basket")))
        view_basket_link.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        # Verify user is redirected to "View Basket" page
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(2)
        checkout_link=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'PROCEED TO CHECKOUT')))
        checkout_link.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='showlogin']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("VCVP@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("VCvp@123<>")
        self.driver.find_element(By.XPATH, "//input[@name='login']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id='billing_first_name']").send_keys("Hinata")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@id='billing_last_name']").send_keys("Shoyo")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@id='billing_company']").send_keys("ssrid")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='billing_email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("new@email.com")
        self.driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("7854120369")
        time.sleep(1)
        # select_country = Select(self.driver.find_element(By.ID, "billing_state"))
        # time.sleep(3)
        # select_country.select_by_visible_text('Canada')
        #time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys("house no 987")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@id='billing_address_2']").send_keys("canada")
        time.sleep(1)
        # select = Select(self.driver.find_element(By.ID, "billing_state"))
        # select.select_by_visible_text('Manitoba')
        self.driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("gfgftdryhfhg")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("110061")
        time.sleep(2)
        place_order_button = self.driver.find_element(By.XPATH, "//input[@id='place_order']")
        place_order_button.click()
        time.sleep(2)
        # verify the addresss is added
        verify_text = self.driver.find_element(By.XPATH, "//p[@class='woocommerce-thankyou-order-received']")
        assert verify_text.text == 'Thank you. Your order has been received.'
        time.sleep(3)

    def test_03_Complete_flow_1_login_from_checkout_page_when_address_data_is_present(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='160']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)

        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        view_basket_link.click()
        time.sleep(2)
        # Verify user is redirected to "View Basket" page
        self.driver.find_element(By.XPATH, "//a[@title='Remove this item']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='showlogin']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Vishal.rana24@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Vishal!24()")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='login']").click()
        time.sleep(1)
        place_order_button = self.driver.find_element(By.XPATH, "//input[@id='place_order']")
        place_order_button.click()
        # verify the addresss is added
        time.sleep(3)
        verify_text = self.driver.find_element(By.XPATH, "//p[@class='woocommerce-thankyou-order-received']")
        assert verify_text.text == 'Thank you. Your order has been received.'

    def test_04_login_user_registered(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys("Vishal.rana24@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Vishal!24()")
        # Click on login button
        Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        Login_submit_button.click()
        time.sleep(1)
        # Verify Login successful
        logout_button = self.driver.find_element(By.LINK_TEXT, 'Logout')
        assert logout_button.text == 'Logout'
        time.sleep(1)
        shop_button = self.driver.find_element(By.LINK_TEXT, "Shop")
        shop_button.click()

    def test_05_new_user_registered(self):
        ######Precondition always provide new reg_email value for success message ################################
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("new_mail02345@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
        time.sleep(1)
        # Click on registration button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(1)
        # Verify register successful
        logout_button = self.driver.find_element(By.LINK_TEXT, 'Logout')
        assert logout_button.text == 'Logout'
        time.sleep(1)
        shop_button = self.driver.find_element(By.LINK_TEXT, "Shop")
        shop_button.click()

    def test_06_update_the_quantity_item(self):
        self.driver.get("https://practice.automationtesting.in/")
    # Add product to cart
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)
        self.driver.get("https://practice.automationtesting.in/basket/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@title='Qty']").clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@title='Qty']").send_keys("10")

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Update Basket']"))
        ).click()
        time.sleep(2)
        upd_message = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-message']")
        if 'updated.' in upd_message.text:
            print("Update item , Item Added")
        else:
            print("not Updated item")

    def test_07_add_two_or_more_items_from_shop(self):
        self.driver.get("https://practice.automationtesting.in/shop/")
        # Add product to cart
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=181']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=170']").click()
        time.sleep(1)
        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(2)
        text1 = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        if text1 == 'Basket Totals':
            print("Pass")
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(2)

    def test_08_add_two_or_more_item_from_home(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='160']")
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button_2 = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        add_to_cart_button_2.click()
        time.sleep(1)
        # Verify "View Basket" link is visible
        # Click on "View Basket" link
        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(2)
        text1 = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        if text1 == 'Basket Totals':
            print("Pass")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(2)

    def test_09_add_item_from_shop_by_clicking_image_box(self):
        self.driver.get("https://practice.automationtesting.in/shop")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 500)")

        implicitly_wait = WebDriverWait(self.driver, 4)
        self.driver.find_element(By.XPATH, "//h3[text()='Thinking in HTML']").click()

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Verify "View Basket" link is visible
        # self.assertTrue(self.is_element_present(By.LINK_TEXT, "View Basket"))
        # Click on "View Basket" link
        time.sleep(2)
        view_basket_link = self.driver.find_element(By.XPATH, "//a[@class='button wc-forward']")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()

    def test_10_add_item_from_home_by_clicking_image_box(self):
        self.driver.get("https://practice.automationtesting.in/")
        # Add product to cart
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")

        self.driver.find_element(By.XPATH, "//h3[text()='Thinking in HTML']").click()

        #time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Verify "View Basket" link is visible
        # Click on "View Basket" link
        time.sleep(3)
        view_basket_link = self.driver.find_element(By.XPATH, "//a[@class='button wc-forward']")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        #time.sleep(3)
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Update Basket']").click()

        time.sleep(1)

    def test_11_add_item_from_shop_by_clicking_product_category_link(self):
        self.driver.get("https://practice.automationtesting.in/shop")
        # Add product to cart
        #self.driver.execute_script("window.scrollTo(0, 1000)")
        # link to go to categories section yaah change

        time.sleep(1)
        link_click=self.driver.find_element(By.XPATH, "//a[text()='HTML']")
        link_click.click()
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(2)
        add_to_cart_button.click()

        # Verify "View Basket" link is visible
        # self.assertTrue(self.is_element_present(By.LINK_TEXT, "View Basket"))
        # Click on "View Basket" link
        time.sleep(2)
        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()

    def test_12_add_an_item_from_shop(self):
        self.driver.get("https://practice.automationtesting.in/shop")
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='170']")
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_button.click()
        # Verify "View Basket" link is visible
        # Click on "View Basket" link
        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(3)
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(5)

    def test_13_add_item_from_home(self):
        self.driver.get("https://practice.automationtesting.in/")
        time.sleep(2)
        # Add product to cart
        self.driver.execute_script("window.scrollTo(0, 1000)")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@data-product_id='163']")
        time.sleep(2)
        add_to_cart_button.click()
        # Verify "View Basket" link is visible
        # Click on "View Basket" link
        time.sleep(1)
        view_basket_link = self.driver.find_element(By.LINK_TEXT, "View Basket")
        time.sleep(1)
        view_basket_link.click()
        # Verify user is redirected to "View Basket" page
        time.sleep(2)
        text = self.driver.find_element(By.XPATH, "//*[text()='Basket Totals']")
        assert text.text == "Basket Totals"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='checkout-button button alt wc-forward']").click()
        time.sleep(2)

    def test_14_new_user_registered_add_billing_address_and_shipping_address(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("new2email12445@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "reg_password").send_keys("frt@!123()trf")
        time.sleep(1)
        # Click on registration button
        registration_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Register']")
        registration_submit_button.click()
        time.sleep(2)
        # Verify register successfful

        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(2)

        # Billing adress:
        self.driver.find_element(By.XPATH, "//a[@class='edit']").click()
        time.sleep(2)

        fname = self.driver.find_element(By.ID, "billing_first_name").send_keys("Hinata")
        lname = self.driver.find_element(By.ID, "billing_last_name").send_keys("Shoyo")
        self.driver.find_element(By.ID, "billing_company").send_keys("ssrid")
        # value = self.driver.find_element(By.ID, "billing_email_field").get_attribute("value")
        # self.assertTrue(value,"f987@gmail.com","Assertion Pass")
        self.driver.find_element(By.ID, "billing_phone").send_keys("7854120369")
        time.sleep(2)
        self.driver.find_element(By.ID, "billing_address_1").send_keys("house no 987")
        self.driver.find_element(By.ID, "billing_address_2").send_keys("Kamla Nagar")
        time.sleep(3)
        # select = Select(self.driver.find_element(By.ID, "billing_state"))
        # select.select_by_visible_text('Manitoba')
        self.driver.find_element(By.ID, "billing_city").send_keys("Telangana")
        self.driver.find_element(By.ID, "billing_postcode").send_keys("110061")

        shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        shop_button.click()
        # verify the addresss is added
        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(3)
        save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'ssrid')]")
        time.sleep(2)
        print(save_data.text)
        time.sleep(3)
        # Shipping adress:
        self.driver.find_element(By.XPATH, "//a[contains(@href,'shipping')]").click()
        time.sleep(3)

        self.driver.find_element(By.ID, "shipping_first_name").send_keys("Hin")
        self.driver.find_element(By.ID, "shipping_last_name").send_keys("Shoy")
        self.driver.find_element(By.ID, "shipping_company").send_keys("Second Home")
        time.sleep(2)
        self.driver.find_element(By.ID, "shipping_address_1").send_keys("house no 987")
        self.driver.find_element(By.ID, "shipping_address_2").send_keys("canada")
        time.sleep(3)
        self.driver.find_element(By.ID, "shipping_city").send_keys("Canda pass")
        self.driver.find_element(By.XPATH, "//input[@id='shipping_postcode']").send_keys("110061")
        shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        shop_button.click()
            # verify the addresss is added
        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(3)
        save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'Second Home')]")
        time.sleep(2)
        print(save_data.text)
        time.sleep(2)
    ##############################Shipping#####################################################3
    def test_15_existing_user_add_shipping_address_by_login_in(self):
            self.driver.get('https://practice.automationtesting.in/my-account/')
            self.driver.find_element(By.ID, "username").send_keys("Vishal.rana24@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("Vishal!24()")
            # Click on login button
            Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
            Login_submit_button.click()
            time.sleep(3)
            # Verify register successfful

            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)

            self.driver.find_element(By.XPATH, "//a[contains(@href,'shipping')]").click()
            time.sleep(3)

            fname = self.driver.find_element(By.ID, "shipping_first_name").send_keys("Vish")
            lname = self.driver.find_element(By.ID, "shipping_last_name").send_keys("Ras")
            self.driver.find_element(By.ID, "shipping_company").send_keys("Home")
            time.sleep(2)
            self.driver.find_element(By.ID, "shipping_address_1").send_keys("house no 1987")
            self.driver.find_element(By.ID, "shipping_address_2").send_keys("delhi")
            time.sleep(3)
            self.driver.find_element(By.ID, "shipping_city").send_keys("gfgftdryhfhg")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//input[@id='shipping_postcode']").send_keys("110061")

            shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
            shop_button.click()
            # verify the addresss is added
            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)
            save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'Home')]")
            time.sleep(2)
            print(save_data.text)

    def test_16_user_shipping_edit_address(self):
            self.driver.get('https://practice.automationtesting.in/my-account/')
            self.driver.find_element(By.ID, "username").send_keys("Vishal.rana24@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("Vishal!24()")
            # Click on login button
            Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
            Login_submit_button.click()
            time.sleep(3)
            # Verify register successfful

            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)

            # Shipping adress:
            self.driver.find_element(By.XPATH, "//a[contains(@href,'shipping')]").click()
            time.sleep(3)

            self.driver.find_element(By.ID, "shipping_first_name").clear()
            self.driver.find_element(By.ID, "shipping_last_name").clear()
            self.driver.find_element(By.ID, "shipping_company").clear()
            time.sleep(2)
            self.driver.find_element(By.ID, "shipping_address_1").clear()
            self.driver.find_element(By.ID, "shipping_address_2").clear()
            time.sleep(3)
            self.driver.find_element(By.ID, "shipping_city").clear()
            self.driver.find_element(By.XPATH, "//input[@id='shipping_postcode']").clear()
            time.sleep(3)
            self.driver.find_element(By.ID, "shipping_first_name").send_keys("Raja")
            self.driver.find_element(By.ID, "shipping_last_name").send_keys("Ram")
            self.driver.find_element(By.ID, "shipping_company").send_keys("Centime Technologies")
            time.sleep(2)
            self.driver.find_element(By.ID, "shipping_address_1").send_keys("house no 1987")
            self.driver.find_element(By.ID, "shipping_address_2").send_keys("delhi")
            time.sleep(3)
            self.driver.find_element(By.ID, "shipping_city").send_keys("Bijwasan")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//input[@id='shipping_postcode']").send_keys("110061")

            shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
            shop_button.click()
            # verify the addresss is added
            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)
            save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'Centime Technologies')]")
            time.sleep(2)
            print(save_data.text)

    def test_17_new_user_registered_add_shipping_address(self):
            self.driver.get('https://practice.automationtesting.in/my-account/')
            self.driver.find_element(By.ID, "reg_email").send_keys("new_shiping_add_user123@gmail.com")
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

            fname = self.driver.find_element(By.ID, "shipping_first_name").send_keys("Hin")
            lname = self.driver.find_element(By.ID, "shipping_last_name").send_keys("Shoy")
            self.driver.find_element(By.ID, "shipping_company").send_keys("WFH")
            time.sleep(2)
            self.driver.find_element(By.ID, "shipping_address_1").send_keys("house no 987")
            self.driver.find_element(By.ID, "shipping_address_2").send_keys("canada")
            time.sleep(3)
            self.driver.find_element(By.ID, "shipping_city").send_keys("gfgftdryhfhg")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//input[@id='shipping_postcode']").send_keys("110061")

            shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
            shop_button.click()
            # verify the addresss is added
            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(3)
            save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'WFH')]")
            time.sleep(2)
            print(save_data.text)

        ########################BILLING ADDRESS####################################################

    def test_19_user_edit_billing_address(self):
            self.driver.get('https://practice.automationtesting.in/my-account/')
            self.driver.find_element(By.ID, "username").send_keys("Vishal.rana24@gmail.com")
            self.driver.find_element(By.ID, "password").send_keys("Vishal!24()")
            # Click on login button
            Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
            Login_submit_button.click()
            time.sleep(2)
            # Verify register successfful

            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(1)

            # Billing adress:
            self.driver.find_element(By.XPATH, "//a[@class='edit']").click()
            time.sleep(1)

            clear_fname = self.driver.find_element(By.ID, "billing_first_name")
            clear_fname.clear()
            time.sleep(1)
            clear_lname = self.driver.find_element(By.ID, "billing_last_name")
            clear_lname.clear()
            clear_company = self.driver.find_element(By.ID, "billing_company")
            clear_company.clear()
            time.sleep(1)
            clear_phone = self.driver.find_element(By.ID, "billing_phone")
            clear_phone.clear()
            clear_address = self.driver.find_element(By.ID, "billing_address_1")
            clear_address.clear()
            time.sleep(1)
            clear_address_2 = self.driver.find_element(By.ID, "billing_address_2")
            clear_address_2.clear()
            clear_city = self.driver.find_element(By.ID, "billing_city")
            clear_city.clear()
            time.sleep(1)
            clear_postcode = self.driver.find_element(By.ID, "billing_postcode")
            clear_postcode.clear()
            time.sleep(1)

            fname = self.driver.find_element(By.ID, "billing_first_name").send_keys("Vishal")
            lname = self.driver.find_element(By.ID, "billing_last_name").send_keys("Rana")
            self.driver.find_element(By.ID, "billing_company").send_keys("srid")
            # value = self.driver.find_element(By.ID, "billing_email_field").get_attribute("value")
            # self.assertTrue(value,"f987@gmail.com","Assertion Pass")
            self.driver.find_element(By.ID, "billing_phone").send_keys("7854120369")
            time.sleep(1)
            self.driver.find_element(By.ID, "billing_address_1").send_keys("house no 987")
            self.driver.find_element(By.ID, "billing_address_2").send_keys("Telagana")
            time.sleep(1)
            self.driver.find_element(By.ID, "billing_city").send_keys("gfgftdryhfhg")
            pincode = self.driver.find_element(By.ID, "billing_postcode").send_keys("110061")

            shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
            shop_button.click()
            # verify the addresss is added
            address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
            address_button.click()
            time.sleep(1)
            save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'srid')]")
            print(save_data.text)

    def test_18_user_login_in_adding_billing(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "username").send_keys("Vishal.rana24@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Vishal!24()")
        # Click on login button
        Login_submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        Login_submit_button.click()
        time.sleep(1)
            # Verify register successfful

        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(1)

        # Billing adress:
        self.driver.find_element(By.XPATH, "//a[@class='edit']").click()
        time.sleep(1)

        fname = self.driver.find_element(By.ID, "billing_first_name").send_keys("Vishal")
        lname = self.driver.find_element(By.ID, "billing_last_name").send_keys("Rana")
        self.driver.find_element(By.ID, "billing_company").send_keys("srid")
        self.driver.find_element(By.ID, "billing_phone").send_keys("7854120369")
        time.sleep(1)
        self.driver.find_element(By.ID, "billing_address_1").send_keys("house no 987")
        self.driver.find_element(By.ID, "billing_address_2").send_keys("Bijwasan")
        time.sleep(1)
        self.driver.find_element(By.ID, "billing_city").send_keys("Telagana")
        pincode = self.driver.find_element(By.ID, "billing_postcode").send_keys("110061")
        shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        shop_button.click()
        # verify the addresss is added
        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(1)
        save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'srid')]")
        time.sleep(1)
        print(save_data.text)

    def test_20_new_user_registered_add_billing_address(self):
        ##############3ENTER NEW Email everytime for rgestering###########################
        self.driver.get('https://practice.automationtesting.in/my-account/')
        self.driver.find_element(By.ID, "reg_email").send_keys("new_user_101112@gmail.com")
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

        fname = self.driver.find_element(By.ID, "billing_first_name").send_keys("ABCDEF")
        lname = self.driver.find_element(By.ID, "billing_last_name").send_keys("Sddeuhue")
        self.driver.find_element(By.ID, "billing_company").send_keys("BSNL")
        self.driver.find_element(By.ID, "billing_phone").send_keys("7854120369")
        time.sleep(1)

        self.driver.find_element(By.ID, "billing_address_1").send_keys("house no 987")
        self.driver.find_element(By.ID, "billing_address_2").send_keys("near railway station")

        time.sleep(1)

        self.driver.find_element(By.ID, "billing_city").send_keys("Raj Nagar")
        self.driver.find_element(By.ID, "billing_postcode").send_keys("154134")

        shop_button = self.driver.find_element(By.XPATH, "//input[@name='save_address']")
        shop_button.click()
        # verify the addresss is added
        address_button = self.driver.find_element(By.LINK_TEXT, 'Addresses')
        address_button.click()
        time.sleep(1)
        save_data = self.driver.find_element(By.XPATH, ".//address[contains(.,'BSNL')]")
        time.sleep(1)
        print(save_data.text)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "_main_":
    unittest.main()