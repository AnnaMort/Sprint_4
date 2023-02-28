from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class PopUpLocators:
    LOCATOR_YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    LOCATOR_NEXT_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")


class ConfPopUP(BasePage):
    def click_yes_button(self):
        yes_button = self.find_element(PopUpLocators.LOCATOR_YES_BUTTON)
        yes_button.click()
        WebDriverWait(driver, 20)
        return yes_button

    def click_next_button(self):
        next_button = self.find_element(PopUpLocators.LOCATOR_NEXT_BUTTON)
        next_button.click()
        WebDriverWait(driver, 20)
        return next_button
