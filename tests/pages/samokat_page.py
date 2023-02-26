from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.base_page import BasePage


class MainLocators:
    LOCATOR_ORDER_TOP_OF_PAGE = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOCATOR_ORDER_BOTTOM_OF_PAGE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOCATOR_IMPORTANT_QUESTION_TEXT = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")


class MainPage(BasePage):
    def click_on_top_button(self):
        return self.find_element(MainLocators.LOCATOR_ORDER_TOP_OF_PAGE).click()

    def click_on_bottom_button(self, driver):
        element = self.find_element(MainLocators.LOCATOR_ORDER_BOTTOM_OF_PAGE)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"))).click()
        return element

    def scroll_till_important_question(self, driver):
        element_question = self.find_element(MainLocators.LOCATOR_IMPORTANT_QUESTION_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", element_question)
        WebDriverWait(driver, 100)
        return element_question
