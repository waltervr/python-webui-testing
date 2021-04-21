class BasePage:
    
    # Constructor that will receive the browser parameter.
    def __init__(self, driver):
        self.driver = driver

    # This method will be reused by all the methods that require interact with an element.
    def get_element(self, element):
        return self.driver.find_element(*element)

    # This method will be return a list of elements.
    def get_elements(self, element):
        return self.driver.find_elements(*element)

    # A method to click on any element, using the local method to find element.
    def click_on_element(self, element):
        self.get_element(element).click()

    # This method will get the element with the local method, then clear the text and insert the new text.
    def type_on_element(self, element, value):
        elem = self.get_element(element)
        elem.clear()
        elem.send_keys(value)
