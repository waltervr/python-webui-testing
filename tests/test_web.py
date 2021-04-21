import pytest

from pages.search import DuckDuckGoSearchPage
from tests.base_test import BaseTest

class TestBasicSearch(BaseTest):

    def test_basic_duckduckgo_search(self):
        # Set up test case data
        PHRASE = "panda"

        # Search for the phrase
        search_page = DuckDuckGoSearchPage(self.driver)
        result_page = search_page.search(PHRASE)

        # Verify that results appear   
        assert result_page.link_div_count() > 0
        assert result_page.phrase_result_count(PHRASE) > 0
        assert result_page.search_input_value() == PHRASE