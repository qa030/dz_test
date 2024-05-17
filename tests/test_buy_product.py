

import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium.webdriver.chrome.options import Options

from pages.payment_page import Payment_page


def test_buy_product():
    # options.add_experimental_option("detach", True)  # чтобы браузер не закрывался
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


    print("Start Test")

    # создаем переменную login в которую поместим экземпляр класса Login_page, в которую передадим driver
    login = Login_page(driver)
    # обратимся к переменной логин login и вызовем метод authorization
    login.authorization()

    # создаем переменную mp которая будет экземпляром класса Main_page и передаем драйвер
    mp = Main_page(driver)
    # обращаемся к экземпляру класса mp и вызываем метод select_product
    mp.select_product()

    # создаем переменную cp которая будет экземпляром класса Cart_page и передаем драйвер
    cp = Cart_page(driver)
    # обращаемся к экземпляру класса cp и вызываем метод product_confirmation
    cp.product_confirmation()

    # создаем переменную cip которая будет экземпляром класса Client_information_page и передаем драйвер
    cip = Client_information_page(driver)
    # обращаемся к экземпляру класса cip и вызываем метод input_information
    cip.input_information()

    # создаем переменную p которая будет экземпляром класса Payment_page и передаем драйвер
    p = Payment_page(driver)
    # обращаемся к экземпляру класса p и вызываем метод input_information
    p.payment()

    # создаем переменную f которая будет экземпляром класса Finish_page и передаем драйвер
    f = Finish_page(driver)
    # обращаемся к экземпляру класса f и вызываем метод Finish_page
    f.finish()



    time.sleep(10)