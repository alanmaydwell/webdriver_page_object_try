"""
Holds identifiers used to identify elements of each page
Imported by pages.py
"""

from selenium.webdriver.common.by import By

# Elements for login screen
login_page = {
    "username":(By.ID, "userField"),
    "password":(By.ID, "passField"),
    "ok_button":(By.CLASS_NAME, "submit"),
    "new_password":(By.LINK_TEXT,
                    "To request a new password or to unlock your account - Click here.")
    }

# Elements for Password request and Account Unlock screen
password_request_page = {
    "username":(By.ID, "userName"),
    "email":(By.ID, "email"),
    "submit_button":(By.CLASS_NAME, "submit")
    }
