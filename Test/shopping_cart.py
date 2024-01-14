from utils.base.base import BaseClass as base

class ShoppingCart(base):
    atc_xpath = "//button[@name='add']"
    view_cart_xpath = "//a[@id='cart-notification-button']"
    increment_xpath = "//button[@name='plus']"
    decrement_xpath = "//button[@name='minus']"
    remove_product_xpath = "//cart-remove-button[@id='Remove-1']"
    continue_shopping_xpath = "//div[@class='cart__warnings']/a[@class='button']"

    def add_product_to_the_cart(self):
        base.wait_for_element_with_xpath_and_click(self, self.atc_xpath)

    def click_on_view_cart_cta(self):
        base.wait_for_element_with_xpath_and_click(self, self.view_cart_xpath)

    def increase_qty_on_cart(self):
        base.wait_for_element_with_xpath_and_click(self, self.increment_xpath)

    def decrease_qty_on_cart(self):
        base.wait_for_element_with_xpath_and_click(self, self.decrement_xpath)

    def remove_product_from_cart(self):
        base.wait_for_element_with_xpath_and_click(self, self.remove_product_xpath)

    def click_on_continue_shopping_cta(self):
        base.wait_for_element_with_xpath_and_click(self, self.continue_shopping_xpath)

