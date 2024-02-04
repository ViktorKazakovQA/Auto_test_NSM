import random
import time

import allure
import pytest
from base.base_test import BaseTest
from selenium.common.exceptions import WebDriverException

@allure.feature("Creat problem functionality")
class Test_ProfileFeature(BaseTest):

    @allure.title("Create NEW Problem")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_create_problems(self):
        try:
            self.NSM_PAGE.open()
        except WebDriverException:
            print("The page does not open")
        self.NSM_PAGE.click_MY_IT()
        self.MYIT_PAGE.is_opened()
        self.MYIT_PAGE.click_still()
        self.MYIT_PAGE.click_create()
        self.MYIT_PAGE.click_problem()
        self.CREATE_PROBLEM_PAGE.is_opened()
        self.CREATE_PROBLEM_PAGE.change_description(f"Auto_Test {random.randint(100,200)}")
        self.CREATE_PROBLEM_PAGE.change_full(f"Auto_Test {random.randint(100,200)}")
        self.CREATE_PROBLEM_PAGE.click_type()
        self.CREATE_PROBLEM_PAGE.click_reactiv()
        self.CREATE_PROBLEM_PAGE.save_problem()
        self.CREATE_PROBLEM_PAGE.new_problem()
