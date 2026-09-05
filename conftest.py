import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.fixture
def navigateToAmazon(page:Page): #green Page is data type #orange colur is fixture
#def navigateToAmazon(page): this also will work
    page.goto("https://www.amazon.in/")
    countOfBtns =page.locator('//*[contains(text(),"Shopping")]').count()
    if countOfBtns>0:
        page.locator('//*[contains(text(),"Shopping")]').click()
       

