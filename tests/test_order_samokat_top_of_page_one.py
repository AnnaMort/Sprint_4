from tests.pages.order_page_for_whom import OrderWhom
from tests.pages.samokat_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.order_page_rent import OrderRent
from tests.pages.order_page_successfull_order_pop_up import ConfPopUP
import allure


@allure.story("tests")
@allure.step("test_order_bottom")
def test_order(driver):
    samokat = MainPage(driver)
    who_order = OrderWhom(driver)
    rent = OrderRent(driver)
    conf_popup = ConfPopUP(driver)

    samokat.click_on_top_button()
    who_order.set_name('Анна')
    who_order.set_last_name('Такаято')
    who_order.set_street('Интересная')
    who_order.set_station()
    who_order.set_phone('2341413412344')
    who_order.click_continue_button()
    rent.set_date()
    rent.set_period()
    rent.choose_color()
    rent.set_comment('Тест')
    rent.click_order_button()
    conf_popup.click_yes_button()
    conf_popup.click_next_button()
    a = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']"))).text
    assert a == 'Отменить заказ'
