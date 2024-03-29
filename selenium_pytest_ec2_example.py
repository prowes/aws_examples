''' Just a simple example of Selenium tests.
To run: pytest [--headed] selenium_pytest_ec2_example.py'''
from selenium import webdriver
import pytest

URL = "https://www.valagroup.com/"


@pytest.fixture()
def setup(request):
    service = webdriver.chrome.service.Service('/usr/bin/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    driver = webdriver.Remote(service.service_url, options=options)
    request.instance.driver = driver

    yield
    driver.close()


@pytest.mark.usefixtures("setup")
class TestURL:
    def test_url_vala(self):
        self.driver.get(URL)
        assert self.driver.title == "Home - VALA"

    def test_failing_koala(self):
        self.driver.get(URL)
        assert self.driver.title == "Home - KOALA"
