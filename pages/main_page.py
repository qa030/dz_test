
import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# класс Main_page будет потомком класса Base
class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    menu = "//button[@class='dropdown-header__button']"
    apple_button = "//a[@href='/catalog/apple']"
    smart_apple_iphone = "//a[@href='apple-iphone']"
    price_min = "//input[@name='pfrom']"
    price_max = "//input[@name='pto']"
    memory = "(//span[@class='txt'])[4]"
    screen = "(//span[@class='txt'])[8]"
    housing_material = "(//span[@class='txt'])[15]"
    cart = "//a[@data-product-id='22683']"


    # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_apple_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple_button)))

    def get_smart_apple_iphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smart_apple_iphone)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_memory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory)))

    def get_screen(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen)))

    def get_housing_material(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.housing_material)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_menu(self):
        self.get_menu().click()
        print("Click Menu")

    def click_apple_button(self):
        self.get_apple_button().click()
        print("Click Apple Button")

    def click_smart_apple_iphone(self):
        self.get_smart_apple_iphone().click()
        print("Click Smart Apple Iphone")

    def input_price_min(self, price_min):
        self.get_price_min().send_keys(price_min)
        print("Input Price Min")

    def input_price_max(self, price_max):
        self.get_price_max().send_keys(price_max)
        print("Input Price Max")

    def click_memory(self):
        self.get_memory().click()
        print("Click Memory")

    def click_screen(self):
        self.get_screen().click()
        print("Click Screen")

    def click_housing_material(self):
        self.get_housing_material().click()
        print("Click Housing Material")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")


    # Methods (шаги которые будем делать в методе)

    def select_product(self):
        self.get_current_url()                                                               # получение текущего url
        self.click_menu()                                                                    # нажимаем на кнопку скрытого меню
        self.click_apple_button()                                                            # нажимаем кнопку apple
        self.click_smart_apple_iphone()                                                      # нажимаем на смартфоны apple iphone
        self.input_price_min("100000")                                                       # вводим минимальную цену
        self.input_price_max("180000")                                                       # вводим максимальную цену
        self.click_memory()                                                                  # ставим фильтр памяти
        self.click_screen()                                                                  # ставим фильтр размер экрана
        self.click_housing_material()                                                        # ставим фильтр материал корпуса
        self.click_cart()                                                                    # нажимаем кнопку перенести корзину