from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    context.browser.get('http://127.0.0.1:5000')

@given('I am on the blog page')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    context.browser.get('http://127.0.0.1:5000/blog')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url



