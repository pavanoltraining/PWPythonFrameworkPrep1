import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from utilities.data_reader_util import read_json_data, read_csv_data, read_excel_data

# Load test data files (adjust paths if needed)

csv_data = read_csv_data("testdata/logindata.csv")
excel_data = read_excel_data("testdata/logindata.xlsx")
json_data = read_json_data("testdata/logindata.json")


# ========================================================
# Data-driven Login Test
# ========================================================

@pytest.mark.parametrize("testName,email, password, expected",csv_data)
#@pytest.mark.parametrize("testName,email, password, expected",excel_data)
#@pytest.mark.parametrize("testName,email, password, expected",json_data)
@pytest.mark.datadriven
def test_login_data_driven(page,testName,email, password, expected):

    # Page object initialization
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # Navigate to Login
    home_page.click_my_account()
    home_page.click_login()

    # Perform login
    login_page.login(email,password)

    # Validation
    if expected == "success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)

