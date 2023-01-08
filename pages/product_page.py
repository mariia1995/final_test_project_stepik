from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)        
        login_link.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")   
        
    def find_the_price_and_name(self):       
        price = self.browser.find_element(*ProductPageLocators.PRICE) 
        price_value = price.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) 
        product_name_value = product_name.text           
        return price_value, product_name_value      

    def find_the_price_and_name_in_basket(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        name_in_basket_value = name_in_basket.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket_value = price_in_basket.text
        return name_in_basket_value, price_in_basket_value