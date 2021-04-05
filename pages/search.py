from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class DuckDuckGoSearchPage(BasePage):
    URL = "https://www.duckduckgo.com"
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        self.type_on_element(self.SEARCH_INPUT, phrase + Keys.RETURN)