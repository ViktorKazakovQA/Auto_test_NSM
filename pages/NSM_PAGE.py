import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class NsmPage(BasePage):

    PAGE_URL = Links.NSM

    MY_IT = ("xpath", "(//a[text() = 'Перейти в Smart IT'])[1]")

    @allure.step("Click MY_IT_PAGE")
    def click_MY_IT(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_IT)).click()