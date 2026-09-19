import allure
from playwright.sync_api import sync_playwright, expect, Page

class homePage:
    def __init__(self,page):
        self.SearchBarTxtBox=page.get_by_placeholder("Search Amazon.in")
        self.cartIcon = page.locator("#nav-cart-count")
        self.logo = page.locator("#nav-logo")
        self.searchSubmitBtn =page.locator("#nav-search-submit-button")

    @allure.step("validateTheVisibilityOfSearchBar") 
    #it is used to see the test body in allure report along with setup and teardown means precondition and postcondition methods
    def validateTheVisibilityOfSearchBar(self):
        expect(self.SearchBarTxtBox).to_be_visible()

    def validateTheVisibilityOfCartIcon(self):
        expect(self.cartIcon).to_be_visible()

    def validateTheVisibilityOfAmazonLogo(self):
        #expect(self.logo).to_be_visible()
        expect(self.logo).to_be_visible()

    def fillSearchBox(self):
        self.SearchBarTxtBox.fill("iphone")

    def clickOnSearchBtn(self):
        self.searchSubmitBtn.click()
