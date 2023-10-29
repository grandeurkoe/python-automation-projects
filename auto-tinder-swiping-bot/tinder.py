import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException

# Tinder username and password stored as environment variables.
TINDER_USERNAME = os.environ['TINDER_USERNAME']
TINDER_PASSWORD = os.environ['TINDER_PASSWORD']


class Tinder:
    def __init__(self, tinder_url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        self.chrome_driver = webdriver.Chrome(chrome_options)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url=tinder_url)
        time.sleep(2)

    def login(self):
        """Logs In to Tinder profile using Facebook. """
        self.chrome_driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(3)

        # Switches between Tinder window and Facebook login popup window.
        main_window_handle = None

        while not main_window_handle:
            main_window_handle = self.chrome_driver.current_window_handle
            try:
                self.chrome_driver.find_element(By.XPATH, value='//*[@id="u91882383"]/main/div[1]/div/div['
                                                                '1]/div/div/div['
                                                                '2]/div[2]/span/div[2]/button').click()
            except NoSuchElementException:
                time.sleep(2)
                self.chrome_driver.find_element(By.XPATH, '//*[@id="u91882383"]/main/div[1]/div/div[1]/div/div/div['
                                                          '2]/div[2]/span/button').click()
                self.chrome_driver.find_element(By.XPATH, value='//*[@id="u91882383"]/main/div[1]/div/div['
                                                                '1]/div/div/div['
                                                                '2]/div[2]/span/div[2]/button').click()
            login_window_handle = None

        while not login_window_handle:
            for handle in self.chrome_driver.window_handles:
                if handle != main_window_handle:
                    login_window_handle = handle
                    break

        self.chrome_driver.switch_to.window(login_window_handle)
        self.chrome_driver.find_element(By.ID, value="email").send_keys(TINDER_USERNAME)
        self.chrome_driver.find_element(By.ID, value="pass").send_keys(TINDER_PASSWORD)
        self.chrome_driver.find_element(By.ID, value="loginbutton").click()
        self.chrome_driver.switch_to.window(main_window_handle)
        time.sleep(8)

        # Gives permission for location and notification settings.
        self.chrome_driver.find_element(By.XPATH, '//*[@id="u91882383"]/main/div[1]/div/div/div[3]/button[1]').click()
        self.chrome_driver.find_element(By.XPATH, '//*[@id="u91882383"]/main/div[1]/div/div/div[3]/button[1]').click()

    def swipe_nope(self):
        """Swipes Not like on Tinder profiles."""
        keep_swiping = True
        swipe_counter = 0
        # Swipes Nope a 100 times.
        while keep_swiping:
            try:
                if swipe_counter == 0:
                    self.chrome_driver.find_element(By.XPATH, '//*[@id="u1820263459"]/div/div[1]/div/main/div['
                                                              '1]/div/div/div['
                                                              '1]/div[1]/div/div[3]/div/div[2]/button').click()
                    swipe_counter += 1
                else:
                    self.chrome_driver.find_element(By.XPATH, '//*[@id="u1820263459"]/div/div[1]/div/main/div['
                                                              '1]/div/div/div['
                                                              '1]/div[1]/div/div[4]/div/div[2]/button').click()
                    swipe_counter += 1
            except ElementNotInteractableException:
                time.sleep(5)
            except NoSuchElementException:
                time.sleep(8)
            except ElementClickInterceptedException:
                time.sleep(5)

            if swipe_counter >= 100:
                keep_swiping = False

        self.chrome_driver.quit()
