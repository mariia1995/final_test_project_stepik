from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    initial_price = page.find_the_price_and_name()[0]
    initial_name = page.find_the_price_and_name()[1]
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    
    assert initial_name == page.find_the_price_and_name_in_basket()[0], "name is incorrect"
    assert initial_price == page.find_the_price_and_name_in_basket()[1], "price is incorrect"
        
    