import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Currency list', self.browser.title)

    def test_add_page(self):
        self.browser.get('http://127.0.0.1:8000/add/')
        self.assertIn('Add currency', self.browser.title)


if __name__ == '__main__':
    unittest.main()