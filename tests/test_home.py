from seleniumbase import BaseCase
import unittest


class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()
        # open home page
        self.open("https://practice.automationbro.com/")

    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        self.inspect_html()
        # Assert logo
        self.assert_element_present("//*[@id='masthead']/div/div/div[1]/div/a/img")
        self.save_screenshot(name="screen")

    def test_home_tab(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")
        # Assert logo
        self.assert_element_present("//*[@id='masthead']/div/div/div[1]/div/a/img")

        self.click("//*[@id='primary']/div/div/div/section[1]/div/div/div/div/div/div[4]/div/div/a/span/span[2]")

        self.save_screenshot(name="screen")


if __name__ == '__main__':
    unittest.main()
