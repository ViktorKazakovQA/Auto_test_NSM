
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ProbemPage(BasePage):

    PAGE_URL = Links.PROBLEM


    DISCRIPTION_FIELD = ("xpath", "//input[ @ title = 'Краткое описание']")
    FULL_DISCRIPTION_FIELD = ("xpath", "//textarea[@placeholder = 'Опишите проблему']")
    # TYPE_PROBLEM_FIELD = ("xpath", "//div[@title-text = 'Тип проблемы']/button")
    TYPE_PROBLEM_FIELD = ("xpath","(//button[@id=''])[6]")
    REACTIV_PROBLEM = ("xpath", "(//div[@title-text = 'Тип проблемы']//a[@role= 'menuitem'])[1]")
    SAVE_BUTTON = ("xpath", "//button[@ng-click = 'createProblem()']")
    NEW_PROBLEM = ("xpath", "//div[@name = 'desc']")
    # NEW_FULL = ("xpath", "//div[@name = 'desc']")

    @allure.step("Enter_description")
    def change_description(self,new_desc):
        description_field = self.wait.until(EC.element_to_be_clickable(self.DISCRIPTION_FIELD))
        description_field.send_keys(new_desc)
        self.name = new_desc
        self.NEW_FULL = ("xpath", f"//div[@title = '{self.name}']")
    @allure.step("Enter_full_description")
    def change_full(self,new_full):
        full_description_field = self.wait.until(EC.element_to_be_clickable(self.FULL_DISCRIPTION_FIELD))
        full_description_field .send_keys(new_full)
        # self.name = new_full

    @allure.step("Click_Type_problem")
    def click_type(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE_PROBLEM_FIELD)).click()


    @allure.step("Click_reactiv")
    def click_reactiv(self):
        self.wait.until(EC.element_to_be_clickable(self.REACTIV_PROBLEM)).click()

    def save_problem(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    # NEW_FULL = ("xpath", f"//div[@title = '{name}']")

    @allure.step("New_problems")
    def new_problem(self):
        # self.wait.until(EC.text_to_be_present_in_element(self.NEW_FULL,self.name))

        self.wait.until(EC.visibility_of_element_located(self.NEW_FULL))
