import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MyitPage(BasePage):

    PAGE_URL = Links.MY_IT


    STILL = ("xpath", "(//a[@data-toggle = 'dropdown'])[2]")
    CREATE = ("xpath", "//div[text() = 'Создать']")
    PROBLEMS  = ("xpath", "//span[text() = 'Проблему']")

    @allure.step("Clik_still")
    def click_still(self):
        self.wait.until(EC.element_to_be_clickable(self.STILL)).click()
    @allure.step("Clik_Create")
    def click_create(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE)).click()

    @allure.step("Clik_Problems")
    def click_problem(self):
        self.wait.until(EC.element_to_be_clickable(self.PROBLEMS)).click()
