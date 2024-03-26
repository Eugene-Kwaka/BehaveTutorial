from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@given(u'User launches the Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


# Specify the parameters using {}. I will replace them with "user" and "pwd"
@when(u'User enters username "{user}" and password "{pwd}"')
def login(context, user, pwd):
    username_elem = context.driver.find_element(By.NAME, "username")
    # Use send_keys() and pass the 'user' and 'pwd' parameters as the arguments
    username_elem.send_keys(user)
    password_elem = context.driver.find_element(By.NAME, "password")
    password_elem.send_keys(pwd)


@when(u'User clicks login button')
def click_login_button(context):
    # Search for the login button and click
    login_button = context.driver.find_element(By.TAG_NAME, "button")
    login_button.click()


@then(u'User successfully logins to the dashboard')
def verify_dashboard_text(context):
    # After login, search for the dashboard text and assert it exists
    dashboard_text = context.driver.find_element(By.TAG_NAME, "h6").text()
    # Assert that dashboard_text == "Dashboard" as seen in the dashboard page
    assert dashboard_text == "Dashboard"
    context.driver.close()
