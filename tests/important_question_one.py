from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.samokat_page import MainPage
from tests.pages.questions_page import Questions


def test_important_question_one(driver):
    samokat = MainPage(driver)
    question = Questions(driver)

    samokat.scroll_till_important_question(driver)
    question.first_question()
    a = WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='accordion__panel-1']"))).text
    assert 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать ' \
           'несколько заказов — один за другим.' == a