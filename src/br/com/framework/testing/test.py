import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print('Setup class - Instantiating chrome driver')
        cls.driver = webdriver.Chrome('../bin/chromedriver.exe')

    def setUp(self):
        print()
        print('Setup - Configuring browser')
        self.driver.maximize_window()

    def test_open_browser(self):
        print()
        print('Testing...')
        self.driver.get('https://www.google.com.br')


    def tearDown(self):
        print()
        print('Tear down')

    @classmethod
    def tearDownClass(cls):
        print()
        print('Tearing down class')
        cls.driver.close()
        try:
            cls.driver.quit()
        except:
            pass

    if __name__ == '__main__':
        unittest.main()