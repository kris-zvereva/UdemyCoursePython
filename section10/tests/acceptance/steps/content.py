from behave import *
from section10.tests.acceptance.page_model.base_page import BasePage
from section10.tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    print(context.browser.page_source)
    assert page.title.is_displayed()

@step('The title tag has content "(.*)"') # step means it can be given when or then
def step_impl(context, content):
    page = BasePage(context.browser)
    print(context.browser.page_source)
    print("Current title text:", page.title.text)  # Debug output
    assert page.title.text == content

@then('I can see there is a post section on the page')
def step_impl(context):
    page = BlogPage(context.browser)
    assert page.posts_section.is_displayed()


