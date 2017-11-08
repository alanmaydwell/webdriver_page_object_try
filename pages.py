"""
Webdriver page definitions for (old) Portal
Used by run_checks.py
"""

from selenium.webdriver.support.ui import WebDriverWait

# Holds locators for each page element
import locators

class BasePage(object):
    """Base class to with attributes common to each page"""

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        """Returns page title"""
        return self.driver.title

    def save_source(self, filename):
        """Write page source"""
        with open(filename, "w") as savefile:
            savefile.write(self.driver.page_source)

class LoginPage(BasePage):

    """
    Login Screen

    """
    # Not sure if we want __init__ here
    # Currently using to auto run self.wait_for_page
    def __init__(self, driver):
        # Call parent class's __init__ - need to forward driver arg to it
        # could use BasePage.__init__(self, driver) but below considered better
        super(LoginPage, self).__init__(driver)
        # Local alias for locators used on this page
        self.locators = locators.login_page
        # Wait for page
        self.wait_for_page()

    def wait_for_page(self, timeout=10):
        """Waits for page to load"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: "https://svspor10ext.laadev.co.uk/fp-war/forgottenPassword.jsp"
            in driver.page_source)

    def type_username(self, username):
        field = self.driver.find_element(*self.locators.get("username"))
        field.clear()
        field.send_keys(username)

    def type_password(self, password):
        field = self.driver.find_element(*self.locators.get("password"))
        field.clear()
        field.send_keys(password)

    def click_go(self):
        button = self.driver.find_element(*self.locators.get("ok_button"))
        button.click()

    def request_new_password(self):
        link = self.driver.find_element(*self.locators.get("new_password"))
        link.click()


class PasswordRequestPage(BasePage):
    """
    Password request and Account Unlock screen
    """
    def __init__(self, driver):
        # Call parent class's __init__ - need to forward driver arg to it
        super(PasswordRequestPage, self).__init__(driver)
        # Local alias for locators used on this page
        self.locators = locators.password_request_page
        # Wait for page
        self.wait_for_page()

    def wait_for_page(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: "A new password will be sent to you by email in a secure PDF document."
            in driver.page_source)

    def type_username(self, username):
        # not keen on below!
        field = self.driver.find_element(*self.locators.get("username"))
        field.clear()
        field.send_keys(username)

    def type_email(self, email):
        # not keen on below!
        field = self.driver.find_element(*self.locators.get("email"))
        field.clear()
        field.send_keys(email)
