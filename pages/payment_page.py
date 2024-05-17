
from webdriver_manager.core import driver

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс Main_page будет потомком класса Base
class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = "//button[@class='button button--big order-confirm__submit']"


    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout Button")

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")
        print("Scroll Down")


    # Methods (шаги которые будем делать в методе)

    def payment(self):
        self.get_current_url()                                    # получение текущего url
        #self.click_checkout_button()                             # нажимаем кнопку оформить заказ
        self.scroll_page()                                        #  прокрутка страницы вниз


