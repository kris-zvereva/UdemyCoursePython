from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from section10.tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')

@given('I wait for the posts to load')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 5).until(
            expected_conditions.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)
        )
    except:
        print(context.browser.page_source)
        raise TimeoutError
