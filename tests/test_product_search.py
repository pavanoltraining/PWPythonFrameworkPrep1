"""
Test Case: Product Search Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Locate the search box on the Home page.
3. Enter a valid product name (for example, "iPhone") in the search box.
4. Click on the "Search" button.
5. Verify that the Search Results page is displayed.
6. Check if the searched product name appears in the list of search results.

Expected Result:
----------------
The Search Results page should appear, and the searched product should be
visible in the search results list.
"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config


@pytest.mark.sanity
@pytest.mark.regression
def test_product_search(page):
    """
    Automated Test Case: Verify that a user can successfully search for a product.
    """

    # --- Test Data ---
    product_name = Config.product_name  # Retrieve product name from configuration file

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)

    # --- Step 1: Enter Product Name in Search Box ---
    home_page.enter_product_name(product_name)

    # --- Step 2: Click on Search Button ---
    home_page.click_search()

    # --- Step 3: Verify Search Results Page is Displayed ---
    expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)

    # --- Step 4: Validate Product Exists in Search Results ---
    expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)
