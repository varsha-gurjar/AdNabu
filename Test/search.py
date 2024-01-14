from utils.base.base import BaseClass as base


class Search(base):
    valid_search_keyword = "Necklace"
    invalid_search_keyword = "123@@@"
    search_icon_xpath = "(//details-modal[@class='header__search'])[1]"
    search_field_xpath = "//input[@id='Search-In-Modal-1']"
    perform_search_xpath = "(//button[@class='search__button field__button'])[1]"
    suggested_product_xpath = "//ul[@id='predictive-search-results-products-list']/li[1]"
    assert_product_name_xpath = "(//h3[@class='card__heading h5'])[1]"

    def click_on_search_icon(self):
        base.wait_for_element_with_xpath_and_click(self, self.search_icon_xpath)

    def open_and_enter_valid_text_in_search_field(self):
        base.wait_for_element_with_xpath_and_click(self, self.search_field_xpath)
        base.wait_for_element_with_xpath(self, self.search_field_xpath).clear()
        base.wait_for_element_with_xpath(self, self.search_field_xpath).send_keys(self.valid_search_keyword)
        self.perform_search()
        product_name = base.wait_for_element_with_xpath(self, self.assert_product_name_xpath).text
        assert self.valid_search_keyword in product_name

    def perform_search(self):
        base.wait_for_element_with_xpath_and_click(self, self.perform_search_xpath)

    def open_and_enter_invalid_text_in_search_field(self):
        base.wait_for_element_with_xpath_and_click(self, self.search_field_xpath)
        base.wait_for_element_with_xpath(self, self.search_field_xpath).clear()
        base.wait_for_element_with_xpath(self, self.search_field_xpath).send_keys(self.invalid_search_keyword)
        self.perform_search()

    def click_on_suggested_product_name(self):
        base.wait_for_element_with_xpath(self, self.search_field_xpath).clear()
        base.wait_for_element_with_xpath(self, self.search_field_xpath).send_keys(self.valid_search_keyword)
        base.wait_for_element_with_xpath_and_click(self, self.suggested_product_xpath)
