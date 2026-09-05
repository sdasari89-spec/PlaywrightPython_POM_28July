from playwright.sync_api import sync_playwright, expect, Page

class resultPage:
    def __init__(self,page):
            self.resultsText=page.locator("//h2[text()='Results']")

    def validateTheVisibilityOfResultstext(self):
        expect(self.resultsText).to_be_visible()