import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Opening browser')
def open_browser(context):
    context.driver = webdriver.Chrome()


@when('Providing google url in browser')
def providing_browser_url(context):
    context.driver.get("https://www.google.com/")


@then('Verify title of the google page')
def verify_title_google(context):
    assert "Google" == context.driver.title


@given('open newtours browser')
def open_netours_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")


@when('provide valid username and password')
def providing_valid_username_password(context):
    time.sleep(2)
    context.driver.find_element(By.NAME, "userName").clear()
    context.driver.find_element(By.NAME, "userName").send_keys("mercury")
    context.driver.find_element(By.NAME, "password").clear()
    context.driver.find_element(By.NAME, "password").send_keys("mercury")
    context.driver.find_element(By.NAME, "submit").click()


@when('provide valid "{username}" and "{password}"')
def providing_valid_username_password(context, username, password):
    time.sleep(2)
    context.driver.find_element(By.NAME, "userName").clear()
    context.driver.find_element(By.NAME, "userName").send_keys(username)
    context.driver.find_element(By.NAME, "password").clear()
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()


@then('verify login is successfull or not')
def verify_success_message(context):
    time.sleep(2)
    assert "Login: Mercury Tours" == context.driver.title


@then('verify success message in login home')
def verify_success_message_login_home(context):
    try:
        message = context.driver.find_element(By.XPATH, "//h3[text()='Login Successfully']").text
        print(message)
    except:
        assert False, "Test Fail"

    if message == "Login Successfully":
        assert True


@when('verify with below query params')
def query_params(context):
    time.sleep(2)
    for r in context.table:
        context.driver.find_element(By.NAME, "userName").clear()
        context.driver.find_element(By.NAME, "userName").send_keys(r["userName"])
        context.driver.find_element(By.NAME, "password").clear()
        context.driver.find_element(By.NAME, "password").send_keys(r["password"])
        context.driver.find_element(By.NAME, "submit").click()