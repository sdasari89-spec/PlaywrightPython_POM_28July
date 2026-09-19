from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import homePage

#data type of fixture is page fixture
#pytest knows page fixture but python doesnot knows about fixtures so suggestions wont appear

#page, cotext, browser , playwright are the data types of playwright

@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
def test_validatepageComponents(page : Page, navigateToAmazon): 
    # orange colour page is called pagfixture and green colour is page datatype to get he suggessions
   # page.goto("https://www.amazon.in/")
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    expect(page).to_have_url("https://www.amazon.in/")

@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
#@allure.feature("home screen testcases")
def test_validateTheVisibilityOfPageComponents(page:Page, navigateToAmazon):

    #searchBar= page.get_by_placeholder("Search Amazon.in")
    #expect(page.get_by_placeholder("Search Amazon.in")).to_be_visible()

    homePageObj=homePage(page)   #page fixture variable is passing to class method mean constructor as a parameter 
    homePageObj.validateTheVisibilityOfSearchBar()
    homePageObj.validateTheVisibilityOfCartIcon()
    homePageObj.validateTheVisibilityOfAmazonLogo()
    # expect(page.locator("#nav-cart-count")).to_be_visible()
    # expect(page.locator("#nav-logo")).to_be_visible()

    #expect(page.get_by_role("link", name="Amazon.in")).to_be_visible()