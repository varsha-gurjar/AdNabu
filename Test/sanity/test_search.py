from Test.search import Search as search


class TestSearch(search):

    def test_search(self):
        self.click_on_search_icon()
        self.open_and_enter_valid_text_in_search_field()
        self.click_on_search_icon()
        self.open_and_enter_invalid_text_in_search_field()
        self.click_on_search_icon()
        self.click_on_suggested_product_name()
