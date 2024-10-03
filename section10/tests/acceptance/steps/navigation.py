from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from section10.tests.acceptance.page_model.blog_page import BlogPage
from section10.tests.acceptance.page_model.home_page import HomePage
from section10.tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    page = HomePage(context.browser)
    context.browser.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    page = BlogPage(context.browser)
    context.browser.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    service = Service('/Users/kristinazvereva/chromedriver')
    context.browser = webdriver.Chrome(service=service)
    page = NewPostPage(context.browser)
    context.browser.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.browser).url
    assert context.browser.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.browser).url
    assert context.browser.current_url == expected_url



