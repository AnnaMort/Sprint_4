from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class RentLocators:
    LOCATOR_WHEN_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")
    LOCATOR_WHEN = (By.XPATH, "//div[contains(text(),'22')]")
    LOCATOR_PERIOD_FIELD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    LOCATOR_PERIOD = (By.XPATH, "//div[contains(text(),'четверо суток')]")
    LOCATOR_CHECKBOX = (By.XPATH, "//input[@id='black']")
    LOCATOR_COMMENT = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[4]/input[1]")
    LOCATOR_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")


class OrderRent(BasePage):
    def set_date(self):
        when_field = self.find_element(RentLocators.LOCATOR_WHEN_FIELD)
        when_field.click()
        WebDriverWait(driver, 10)
        date = self.find_element(RentLocators.LOCATOR_WHEN)
        date.click()
        return date

    def set_period(self):
        period_field = self.find_element(RentLocators.LOCATOR_PERIOD_FIELD)
        period_field.click()
        WebDriverWait(driver, 10)
        period = self.find_element(RentLocators.LOCATOR_PERIOD)
        period.click()
        return period

    def choose_color(self):
        color = self.find_element(RentLocators.LOCATOR_CHECKBOX)
        color.click()
        return color

    def set_comment(self, comment):
        set_text = self.find_element(RentLocators.LOCATOR_COMMENT)
        set_text.send_keys(comment)
        return set_text

    def click_order_button(self):
        order_button = self.find_element(RentLocators.LOCATOR_ORDER_BUTTON)
        order_button.click()
        WebDriverWait(driver, 30)
        return order_button

