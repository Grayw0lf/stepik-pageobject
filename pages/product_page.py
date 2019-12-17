import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADDING_GOODS_TO_BASKET)
        cart.click()

    def price_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_check = self.browser.find_element(*ProductPageLocators.PRICE_CHECK).text
        assert price == price_check, "Price is't correct!"

    def items_correct(self):
        item = self.browser.find_element(*ProductPageLocators.GOOD).text
        items_check = self.browser.find_element(*ProductPageLocators.GOOD_CHECK).text
        assert item == items_check, "Wrong item or name of item!"
