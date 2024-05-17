

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс Main_page будет потомком класса Base
class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    # Getters


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)


    # Methods (шаги которые будем делать в методе)

    def finish(self):
        self.get_current_url()                                                          # получение текущего url
        self.assert_url('https://biggeek.ru/cart')                                      # проверка url
        self.get_screenshot()                                                           # сохранить скриншот
