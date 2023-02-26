from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class WhoOrderLocators:
    LOCATOR_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/input[@value]")
    LOCATOR_LAST_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/input[@value]")
    LOCATOR_STREET = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/input[@value]")
    LOCATOR_STATION_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/input[1]")
    LOCATOR_STATION_NAME = (By.XPATH, "//div[contains(text(),'Сокольники')]")
    LOCATOR_PHONE = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[5]/input[@value]")
    LOCATOR_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")


class OrderWhom(BasePage):
    def set_name(self, name):
        n = self.find_element(WhoOrderLocators.LOCATOR_NAME)
        n.send_keys(name)
        return n

    def set_last_name(self, last):
        last_name = self.find_element(WhoOrderLocators.LOCATOR_LAST_NAME)
        last_name.send_keys(last)
        return last_name

    def set_street(self, st):
        street_n = self.find_element(WhoOrderLocators.LOCATOR_STREET)
        street_n.send_keys(st)
        return street_n

    def set_station(self):
        field = self.find_element(WhoOrderLocators.LOCATOR_STATION_FIELD)
        field.click()
        WebDriverWait(driver, 40)
        station_name = self.find_element(WhoOrderLocators.LOCATOR_STATION_NAME)
        station_name.click()
        return station_name

    def set_phone(self, phone):
        numb = self.find_element(WhoOrderLocators.LOCATOR_PHONE)
        numb.send_keys(phone)
        return numb

    def click_continue_button(self):
        button = self.find_element(WhoOrderLocators.LOCATOR_BUTTON)
        button.click()
        WebDriverWait(driver, 30)
        return button
