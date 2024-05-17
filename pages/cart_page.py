

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс Main_page будет потомком класса Base
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_button = "//a[@class='button button--medium cart-modal__cart-link']"
    test_word = "//a[@href='/products/apple-iphone-15-pro-256gb-sinij-titan-blue-titanium']"


    # Getters

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_test_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_word)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")


    # Methods (шаги которые будем делать в методе)

    def product_confirmation(self):
        self.get_current_url()                                                                                               # получение текущего url
        self.click_cart_button()                                                                                             # нажимаем на кнопку корзины
        self.assert_word(self.get_test_word(), "Смартфон Apple iPhone 15 Pro 256 ГБ («Синий титан» | Blue Titanium)")        # вызываем метод с проверкой по слову

