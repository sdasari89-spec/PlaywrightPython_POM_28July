from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.homePage import homePage
from pages.resultPage import resultPage

@pytest.mark.results
@pytest.mark.smoke
@pytest.mark.regression
def test_validateTheResultsUI(page : Page, navigateToAmazon): 

    homePageObj=homePage(page)  
    homePageObj.fillSearchBox()
    homePageObj.clickOnSearchBtn()

    resultsPageObj=resultPage(page) 
    resultsPageObj.validateTheVisibilityOfResultstext() 

    
    #page.get_by_placeholder("Search Amazon.in").fill("iphone")
    #page.locator("#nav-search-submit-button").click()
    #print(page.title())
    #expect(page.locator("//h2[text()='Results']")).to_be_visible()
    expect(page).to_have_title("Amazon.in : iphone")