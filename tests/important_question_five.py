from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.samokat_page import MainPage
from tests.pages.questions_page import Questions
import allure


@allure.story("tests")
@allure.step("test_order_bottom")
def test_important_question_five(driver):
    samokat = MainPage(driver)
    question = Questions(driver)

    samokat.scroll_till_important_question(driver)
    question.fifth_question()
    a = WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='accordion__panel-5']"))).text
    assert a == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься ' \
                'без передышек и во сне. Зарядка не понадобится.'
