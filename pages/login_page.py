
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# класс Login_page будет потомком класса Base
class Login_page(Base):

    url = 'https://biggeek.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_registration_button = "//a[@class='user-header-middle__link user-header-middle__link--sing-in login-modal-singin']"
    user_name = "//input[@id='singin-email']"
    password = "//input[@id='singin-password']"
    login_button = "//button[@class='button button--small login-modal__login-submit']"
    main_word = "//a[@class='user-header-middle__link user-header-middle__link--account']"


    # Getters

    def get_login_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_registration_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions (действия которые будем выполнять с локаторами, кликать, заполнять поля, перемещать)

    def click_login_registration_button(self):
        self.get_login_registration_button().click()
        print("Click Login/Registration Button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input User Name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")


    # Methods (шаги которые будем делать в методе)

    def authorization(self):
        self.driver.get(self.url)                                           # открывает страницу
        self.driver.maximize_window()                                       # максимальное открытие браузера
        self.get_current_url()                                              # получение текущего url
        self.click_login_registration_button()                              # нажимаем на конопку вход/регистрация
        self.input_user_name("karpov.sti@bk.ru")                                          # заполняем логин
        self.input_password("Test808")                                      # заполняем пароль
        self.click_login_button()                                           # нажимаем кнопку войти
        self.assert_word(self.get_main_word(), "Личный кабинет")                          # вызываем метод с проверкой по слову
