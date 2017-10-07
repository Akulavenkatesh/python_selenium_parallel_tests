import unittest
from time import sleep
from selenium import webdriver


class TestParallel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
            })
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("https://www.google.org")
        sleep(5)

    def test_two(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()