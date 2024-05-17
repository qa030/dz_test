

import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method get current url, получение текущего url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        # print("Current url + get_urk")
        print(f"Current url {get_url}")


    """Method assert word, проверка авторизации по слову """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value Word")


    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\Серёга\\PycharmProjects\\dz_finish\\screen\\' + name_screenshot)


    """Method assert url, проверка по url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good Value Url")


