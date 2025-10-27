"""
Test Case: User Login Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify Login with Invalid Credentials
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter an invalid email address and password.
5. Click on the "Login" button.
6. Verify that an error message appears indicating invalid credentials.

Expected Result:
----------------
An error message should be displayed, and the user should not be logged in.


Test Case 2: Verify Login with Valid Credentials
------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Verify that the "My Account" page is displayed after successful login.

Expected Result:
----------------
The "My Account" page should appear, confirming a successful login.
"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Config  # Configuration file holding credentials


@pytest.mark.sanity
@pytest.mark.regression
def test_invalid_user_login(page):
    """
    Automated Test Case: Verify that login fails for invalid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 2: Enter Invalid Credentials ---
    login_page.set_email(Config.invalid_email)
    login_page.set_password(Config.invalid_password)
    login_page.click_login()

    # --- Step 3: Verify Login Failure ---
    # Expect an error message to appear due to invalid credentials
    expect(login_page.get_login_error()).to_be_visible(timeout=3000)


@pytest.mark.sanity
@pytest.mark.regression
def test_valid_user_login(page):
    """
    Automated Test Case: Verify that login succeeds for valid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 2: Enter Valid Credentials ---
    login_page.set_email(Config.email)
    login_page.set_password(Config.password)
    login_page.click_login()

    # Wait for the page to load completely after login
    time.sleep(3)

    # --- Step 3: Verify Successful Login ---
    # Expect the "My Account" page heading to be visible
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
