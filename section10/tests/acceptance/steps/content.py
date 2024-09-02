from behave import *
from selenium.webdriver.common.by import By


use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert title_tag.is_displayed()


@step('The title tag has content "(.*)"') # step means it can be given when or then
def step_impl(context, content):
    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert title_tag.text == content
