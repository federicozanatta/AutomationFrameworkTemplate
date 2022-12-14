import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(executable_path='utilities\chromedriver.exe')
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        # driver = webdriver.Firefox()
        print("Launching edge browser.........")
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = driver=webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\PytestHybridframework\\utilites\\chromedriver.exe')
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                                   # this will return the browser value to setup method
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure (config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'khemlall'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)