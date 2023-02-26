from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.samokat_page import MainPage
from tests.pages.questions_page import Questions


def test_important_question_four(driver):
    samokat = MainPage(driver)
    question = Questions(driver)

    samokat.scroll_till_important_question(driver)
    question.fourth_question()
    a = WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='accordion__panel-4']"))).text
    assert a == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
