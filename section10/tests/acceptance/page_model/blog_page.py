from section10.tests.acceptance.locators.blog_page import BlogPageLocators
from section10.tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.browser.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.browser.find_elements(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.browser.find_element(*BlogPageLocators.NEW_POST_LINK)
