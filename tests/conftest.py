import pytest
from selenium.webdriver import Chrome, Firefox
from generics.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    # Initialize WebDriver
    if TestData.BROWSER == "chrome":
        web_driver = Chrome()
    elif TestData.BROWSER == "firefox":
        web_driver = Firefox()
    else:
        raise Exception(f'"{TestData.BROWSER}" is not supported browser')
    
    # Create a global instance of the driver for every execution
    request.cls.driver = web_driver

    # Maximize the window
    web_driver.maximize_window()

    # Open the URL
    web_driver.get(TestData.APP_URL)

    # Return the driver object at the end of setup
    yield web_driver
    
    # For cleanup, quit the driver
    web_driver.quit()