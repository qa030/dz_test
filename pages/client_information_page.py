from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# класс Login_page будет потомком класса Base
class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    first_name = "//input[@id='name']"
    last_name = "//input[@id='last-name']"
    mail = "//input[@id='email']"
    mobile_phone = "//input[@id='phone']"
    pickup = "//button[@class='order-form__tab order-form__tab--current']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_mobile_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phone)))

    def get_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input Mail")

    def input_mobile_phone(self, mobile_phone):
        self.get_mobile_phone().send_keys(mobile_phone)
        print("Input Mobile Phone")

    def click_pickup(self):
        self.get_pickup().click()
        print("Click Pickup")


    # Methods (шаги которые будем делать в методе)

    def input_information(self):
        self.get_current_url()                                          # получение текущего url
        self.input_first_name("Ivan")                                   # заполняем логин
        self.input_last_name("Ivanov")                                  # заполняем пароль
        self.input_mail("test@bk.ru")                                   # заполняем электронную почту
        self.input_mobile_phone("920 999 00 00")                        # заполняем поле телефон
        self.click_pickup()                                             # нажимаем кнопку самовывоз

