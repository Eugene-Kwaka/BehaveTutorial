from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when(u'user opens Orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then(u'verify that logo is present')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img').is_displayed()
    assert status is True

@then(u'close browser')
def close_browser(context):
    context.driver.close()
