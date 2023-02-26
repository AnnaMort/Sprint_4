from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.samokat_page import MainPage
from tests.pages.questions_page import Questions

def test_important_question_six(driver):
    samokat = MainPage(driver)
    question = Questions(driver)

    samokat.scroll_till_important_question(driver)
    question.sixth_question()
    a = WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='accordion__panel-6']"))).text
    assert a == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
