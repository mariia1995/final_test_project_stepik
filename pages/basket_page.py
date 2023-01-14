from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class BasketPage(BasePage):
    def should_not_be_any_product(self):      
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product is presented, but should not be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Message that the basket is empty is not presented, but should be"
        