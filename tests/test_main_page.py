import pytest
import allure
import data
from data import DataFAQ
from pages.main_page import MainPage



class TestMainPage:
    @allure.title('Проверка вопросов и ответов')
    @allure.description('Кликаем на вопрос, получаем ответ, сравниваем с ожидаемым ответом')
    @pytest.mark.parametrize("number, question, expected_answer", DataFAQ.ANSWERS)
    def test_answer_for_question(self, driver, number, question, expected_answer):
        main_page = MainPage(driver)
        main_page.close_cookies()
        main_page.click_on_faq(number)

        actual_answer = main_page.get_faq_text_answers(number)
        assert actual_answer == expected_answer
