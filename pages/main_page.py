import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators


#класс содержит методы главной страницы и наследует базовые методы
class MainPage(BasePage):

#кликаем на вопрос
    @allure.step('Кликаем на вопрос')
    def click_on_faq(self, question_number):
         self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS[question_number])
         self.click_to_element(MainPageLocators.FAQ_QUESTIONS[question_number])

#получаем текст ответа
    @allure.step('Получаем текст ответа')
    def get_faq_text_answers(self, answer_number):
        return self.get_text_from_element(MainPageLocators.FAQ_ANSWERS[answer_number])

#принятие куки, клик по кнопке "Заказать" в теле на главной странице
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в теле на главной странице')
    def click_button_order_in_body_of_main_page_and_transition_to_order_page(self):
        self.close_cookies()
        self.click_to_element(MainPageLocators.button_order_locator)
        self.find_element(OrderPageLocators.fields_name_locator)

#метод закрытие окна с куками
    @allure.step('Закрытие окна с куками')
    def close_cookies(self):
        self.windows_cookies(BasePageLocators.button_accept_cookie_locator).click()


#принятие куки, клик по кнопке "Заказать" в заголовке
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в хедере')
    def click_order_button_in_header_and_transition_to_order_page(self):
        self.close_cookies()
        self.click_to_element(BasePageLocators.button_order_header_locator)
        self.find_element(OrderPageLocators.fields_name_locator)
