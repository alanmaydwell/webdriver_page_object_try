# webdriver_page_object_try
Attempt at using webdriver with a Page Object approach.    

- Partly based on information here: http://selenium-python.readthedocs.io/page-objects.html but with some differences.
- Interacts with test version of (old) LAA Portal.    
- usernames/passwords in scripts are fake.

## run_portal_checks.py
Execute this to run the checks.
Uses Python unittest.TestCase.

## pages.py
Contains page definitions.
Imported by run_portal_checks.py

## locators.py
Contains element locator definitions.
Imported by pages.py

