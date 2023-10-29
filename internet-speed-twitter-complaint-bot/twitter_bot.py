import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Twitter email, username and password stored as environmental variables.
TWITTER_URL = "https://twitter.com/i/flow/login?lang=en"
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']
TWITTER_USERNAME = os.environ['TWITTER_USERNAME']


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        self.chrome_driver = webdriver.Chrome(chrome_options)
        self.chrome_driver.maximize_window()

    def get_internet_speed(self):
        """Gets internet speed from Speedtest.net."""
        self.chrome_driver.get(SPEEDTEST_URL)
        self.chrome_driver.find_element(By.LINK_TEXT, "GO").click()
        time.sleep(40)
        self.down = self.chrome_driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                              '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                              '1]/div/div[2]/span').text
        self.up = self.chrome_driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '2]/div/div[2]/span').text

    def tweet_at_provider(self, promised_up, promised_down):
        """Tweets at the ISP, if promised internet speed is not met."""

        # Sign In To Twitter.
        self.chrome_driver.get(TWITTER_URL)

        time.sleep(3)
        twitter_email = self.chrome_driver.find_element(By.XPATH,
                                                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                        '2]/div/input')
        twitter_email.send_keys(TWITTER_EMAIL)
        twitter_email.send_keys(Keys.ENTER)

        time.sleep(3)
        twitter_username = self.chrome_driver.find_element(By.XPATH,
                                                           '//*[@id="layers"]/div/div/div/div/div/div/div['
                                                           '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                           '2]/label/div/div[2]/div/input')
        twitter_username.send_keys(TWITTER_USERNAME)
        twitter_username.send_keys(Keys.ENTER)

        time.sleep(3)
        twitter_password = self.chrome_driver.find_element(By.XPATH,
                                                           '//*[@id="layers"]/div/div/div/div/div/div/div['
                                                           '2]/div[2]/div/div/div[2]/div[2]/div['
                                                           '1]/div/div/div[3]/div/label/div/div[2]/div['
                                                           '1]/input')
        twitter_password.send_keys(TWITTER_PASSWORD)
        twitter_password.send_keys(Keys.ENTER)

        tweet = (f"Hey Internet Provider, why is internet speed {self.down}down/{self.up}up when I pay for "
                 f"{promised_down}down/{promised_up}up?")

        time.sleep(10)

        # Tweet to ISP.
        navigate = ActionChains(self.chrome_driver)
        navigate.move_to_element(self.chrome_driver.find_element(By.CLASS_NAME, 'DraftEditor-root')).click().perform()
        navigate.send_keys(tweet).perform()
        navigate.move_to_element(self.chrome_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                                           '2]/main/div/div/div/div[1]/div/div['
                                                                           '3]/div/div[2]/div[1]/div/div/div/div['
                                                                           '2]/div[2]/div[2]/div/div/div[2]/div['
                                                                           '3]/div/span/span')).click().perform()
