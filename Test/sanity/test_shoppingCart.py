from Test.shopping_cart import ShoppingCart


class TestShoppingCart(ShoppingCart):
    pdp_url = "https://adnabu-arjun.myshopify.com/products/18k-fluid-lines-necklace"
    plp_url = "https://adnabu-arjun.myshopify.com/collections/all"

    def test_cart(self):
        self.go_to_url(self.pdp_url)
        self.add_product_to_the_cart()
        self.click_on_view_cart_cta()
        self.increase_qty_on_cart()
        self.decrease_qty_on_cart()
        self.remove_product_from_cart()
        self.click_on_continue_shopping_cta()
        assert self.driver.current_url == self.plp_url
