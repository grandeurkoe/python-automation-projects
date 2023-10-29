import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os

# Instagram username and password are stored as environment variables.
INSTAGRAM_URL = "https://www.instagram.com/"
INSTA_USERNAME = os.environ['INSTA_USERNAME']
INSTA_PASSWORD = os.environ['INSTA_PASSWORD']


class InstaFollower:
    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        self.chrome_driver = webdriver.Chrome(chrome_options)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(INSTAGRAM_URL)

    def login(self, search_query):
        """Logins to Instagram account. Searches for Instagram account based on the search query provided."""

        # Login to Instagram account.
        time.sleep(3)
        username_entry = self.chrome_driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_entry.send_keys(INSTA_USERNAME)

        password_entry = self.chrome_driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_entry.send_keys(INSTA_PASSWORD)

        time.sleep(2)
        self.chrome_driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

        # Searches for instagram account based on search_query.
        time.sleep(5)
        search_bar = self.chrome_driver.find_element(By.LINK_TEXT, 'Search')
        search_bar.click()

        time.sleep(1)
        search_navigate = ActionChains(self.chrome_driver)
        search_navigate.send_keys(search_query).perform()

        time.sleep(2)
        search_navigate.send_keys(Keys.DOWN).perform()
        search_navigate.send_keys(Keys.ENTER).perform()

    def find_followers(self):
        """Gets the Instagram account of every follower. Returns the follower list."""
        time.sleep(5)
        self.chrome_driver.find_element(By.PARTIAL_LINK_TEXT, 'followers').click()

        time.sleep(2)
        follower_popup = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div['
                                                                   '2]/div/div/div/div/div[2]/div/div/div[3]')

        # Scrolls a certain number of times in the follower popup window.
        follower_scroll = 0
        while follower_scroll < 1:
            self.chrome_driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments["
                                              "0].offsetHeight;", follower_popup)
            time.sleep(1)
            follower_scroll += 1

        follower_list = self.chrome_driver.find_elements(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > '
                                                                          'div.x9f619.x1n2onr6.x1ja2u2z > div > '
                                                                          'div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf'
                                                                          '.xaigb6o.x12ejxvf.x3igimt.xarpa2k'
                                                                          '.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs'
                                                                          '.x1n2onr6.x1qrby5j.x1jfb8zj > div > '
                                                                          'div > div > div > '
                                                                          'div.x7r02ix.xf1ldfh.x131esax.xdajt7p'
                                                                          '.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f'
                                                                          '.x5fp0pe > div > div > div._aano button')
        return follower_list

    def follow(self, follower_list):
        """Follows every Instagram account on the follower list."""
        for follower in follower_list:
            try:
                follower.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.chrome_driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div['
                                                          '2]/div/div/div/div/div/div/button[2]').click()
                time.sleep(2)

        # Close the follower popup window after following everyone on the follower list.
        self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div['
                                                  '2]/div/div/div[1]/div/div[3]/div/button').click()
