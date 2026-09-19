import allure
import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.fixture
def navigateToAmazon(page:Page): #green Page is data type #orange colur is fixture
#def navigateToAmazon(page): this also will work
    page.goto("https://www.amazon.in/")
    countOfBtns =page.locator('//*[contains(text(),"Shopping")]').count()
    if countOfBtns>0:
        page.locator('//*[contains(text(),"Shopping")]').click()
       

# fixture will execute before ech and every testcase
#hook will execute when the testcase failed and take the screenshot an dwill show in allure report
#it will directly communicate with allure
#hook WIL EXECUTE before execution of THE SEESION AND ENTIRE TESTCASES

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item): #item means testcase
    outcome = yield #wait for the testcase execution and store the entire testcase results in outcome 
    report=outcome.get_result() #give th edetails pass or fail 
    if report.failed:
        page=item.funcargs.get("page")  #capture the current page and store in the variable page
        if page:allure.attach(page.screenshot(),name="failed page",attachment_type=allure.attachment_type.PNG)

# def pytest_sessionstart(session):
#     with open("allure-results/environmnet.properties","w")as f:
#        f.write("regression report\n")