from selenium.webdriver.common.by import By

class MainPageLocators:    #класс содержит локаторы главной страницы

    #кнопка "Заказать" в теле страницы
    button_order_locator = By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    check_yandex_dzen = By.XPATH, './/*[@class="dzen-layout--navigation-tab__tabWrapper-3L"]'

    FAQ_QUESTIONS = {
        1: (By.ID, "accordion__heading-0"),
        2: (By.ID, "accordion__heading-1"),
        3: (By.ID, "accordion__heading-2"),
        4: (By.ID, "accordion__heading-3"),
        5: (By.ID, "accordion__heading-4"),
        6: (By.ID, "accordion__heading-5"),
        7: (By.ID, "accordion__heading-6"),
        8: (By.ID, "accordion__heading-7")
    }

    FAQ_ANSWERS = {
        1: (By.ID, "accordion__panel-0"),
        2: (By.ID, "accordion__panel-1"),
        3: (By.ID, "accordion__panel-2"),
        4: (By.ID, "accordion__panel-3"),
        5: (By.ID, "accordion__panel-4"),
        6: (By.ID, "accordion__panel-5"),
        7: (By.ID, "accordion__panel-6"),
        8: (By.ID, "accordion__panel-7")
    }
