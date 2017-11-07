#!/usr/bin/env python

import unittest
from selenium import webdriver

# Holds page object definitions
import pages

class SeleniumRun(unittest.TestCase):
    """Attempt at using Page Object Approach

    Relies on page elements recorded in pages module

    Note present class is derived from unittest.TestCase class:
        Calling unittest.main() runs each method with name starting "test"
        Doesn't seem any need to specify class name, unittest.main() finds
        out via some obscure means of its own!
        Additionaly - setUP method auto called before each
                    - tearDown called after each
    """

    def setUp(self):
        """
        Auto runs before each test method
        (setUp name is standard, although deviates from PEP8)
        """
        self.driver = webdriver.Firefox()
        self.driver.get("https://svssso10ext.laadev.co.uk")

    def test_do_things_on_page(self):
        """
        Eneters details on Portal
        """

        # Load the login page. In this case the home page of Python.org.
        login_page = pages.LoginPage(self.driver)
        # Type username and password on page
        login_page.type_username("Galuthrax")
        login_page.type_password("shazam!")
        # Select password reset screen
        login_page.request_new_password()
        # Pick up new screen
        password_page = pages.PasswordRequestPage(self.driver)
        # Type username and email address
        password_page.type_username("Galuthrax")
        password_page.type_email("a.b@c.com")


    def tearDown(self):
        """Auto runs after each test method
        (tearDown name is standard, although deviates from PEP8)
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
