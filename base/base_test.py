import pytest

from pages.NSM_PAGE import NsmPage
from pages.MYIT_PAGE import MyitPage
from pages.CREATE_PROBLEM_PAGE import ProbemPage

class BaseTest:

    NSM_PAGE: NsmPage
    MYIT_PAGE: MyitPage
    CREATE_PROBLEM_PAGE: ProbemPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.NSM_PAGE = NsmPage(driver)
        request.cls.MYIT_PAGE = MyitPage(driver)
        request.cls.CREATE_PROBLEM_PAGE = ProbemPage(driver)
