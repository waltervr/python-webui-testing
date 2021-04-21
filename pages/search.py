from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.result import DuckDuckGoResultPage

class DuckDuckGoSearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, phrase):
        self.type_on_element(self.SEARCH_INPUT, phrase + Keys.RETURN)
        return DuckDuckGoResultPage(self.driver)