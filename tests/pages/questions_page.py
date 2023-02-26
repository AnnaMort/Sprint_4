from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class QuestionsLocators:
    LOCATOR_Q_0 = (By.XPATH, "//div[@id='accordion__heading-0']")
    LOCATOR_Q_1 = (By.XPATH, "//div[@id='accordion__heading-1']")
    LOCATOR_Q_2 = (By.XPATH, "//div[@id='accordion__heading-2']")
    LOCATOR_Q_3 = (By.XPATH, "//div[@id='accordion__heading-3']")
    LOCATOR_Q_4 = (By.XPATH, "//div[@id='accordion__heading-4']")
    LOCATOR_Q_5 = (By.XPATH, "//div[@id='accordion__heading-5']")
    LOCATOR_Q_6 = (By.XPATH, "//div[@id='accordion__heading-6']")
    LOCATOR_Q_7 = (By.XPATH, "//div[@id='accordion__heading-7']")


class Questions(BasePage):
    def zero_question(self):
        question_zero = self.find_element(QuestionsLocators.LOCATOR_Q_0)
        question_zero.click()
        WebDriverWait(driver, 40)
        return question_zero

    def first_question(self):
        question_first = self.find_element(QuestionsLocators.LOCATOR_Q_1)
        question_first.click()
        WebDriverWait(driver, 40)
        return question_first

    def second_question(self):
        question_second = self.find_element(QuestionsLocators.LOCATOR_Q_2)
        question_second.click()
        WebDriverWait(driver, 40)
        return question_second

    def third_question(self):
        question_third = self.find_element(QuestionsLocators.LOCATOR_Q_3)
        question_third.click()
        WebDriverWait(driver, 40)
        return question_third

    def fourth_question(self):
        question_fourth = self.find_element(QuestionsLocators.LOCATOR_Q_4)
        question_fourth.click()
        WebDriverWait(driver, 40)
        return question_fourth

    def fifth_question(self):
        question_fifth = self.find_element(QuestionsLocators.LOCATOR_Q_5)
        question_fifth.click()
        WebDriverWait(driver, 40)
        return question_fifth

    def sixth_question(self):
        question_sixth = self.find_element(QuestionsLocators.LOCATOR_Q_6)
        question_sixth.click()
        WebDriverWait(driver, 40)
        return question_sixth

    def seventh_question(self):
        question_seventh = self.find_element(QuestionsLocators.LOCATOR_Q_7)
        question_seventh.click()
        WebDriverWait(driver, 40)
        return question_seventh

