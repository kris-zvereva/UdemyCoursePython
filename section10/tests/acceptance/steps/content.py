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
    assert page.title.text == content

@then('I can see there is a post section on the page')
def step_impl(context):
    page = BlogPage(context.browser)
    assert page.posts_section.is_displayed()

@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.browser)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])  # all is a builtin function in python, opposite - any()


