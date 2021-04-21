from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DuckDuckGoResultPage(BasePage):
    LINK_DIVS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, driver):
        super().__init__(driver)

    def link_div_count(self):
        return len(self.get_elements(self.LINK_DIVS))

    def phrase_result_count(self, phrase):
        return len(self.get_elements(self.PHRASE_RESULTS(phrase)))

    def search_input_value(self):
        search_input = self.get_element(self.SEARCH_INPUT)
        return search_input.get_attribute("value")