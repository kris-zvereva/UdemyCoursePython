from section10.tests.acceptance.locators.home_page import HomePageLocators
from section10.tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.browser.find_element(*HomePageLocators.NAVIGATION_LINK)
