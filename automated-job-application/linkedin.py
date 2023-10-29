import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.expected_conditions import NoSuchElementException

# LINKEDIN email and password stored as environment variables.
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class LinkedIn:
    def __init__(self, job_search_query):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option(name="detach", value=True)

        self.chrome_driver = webdriver.Chrome(self.chrome_options)
        self.chrome_driver.maximize_window()

        self.chrome_driver.get(url=job_search_query)

    def sign_in(self):
        """Signs in to LinkedIn."""
        self.chrome_driver.find_element(By.ID, value="session_key").send_keys(MY_EMAIL)
        password_input = self.chrome_driver.find_element(By.ID, value="session_password")
        password_input.send_keys(MY_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(15)

    def search_job_query(self):
        """Searches for job listings."""
        search_box = self.chrome_driver.find_element(By.XPATH,
                                                     value='/html/body/div[5]/header/div/div/div/div[1]/input')
        search_box.send_keys("python developer")
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        self.chrome_driver.find_element(By.XPATH,
                                        value='/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button').click()
        time.sleep(5)
        self.chrome_driver.find_element(By.CSS_SELECTOR, value='.search-reusables__filter-binary-toggle button').click()
        time.sleep(5)

    def save_job_posting(self):
        """Saves all job listings and follows each company whose job is listed."""
        section = self.chrome_driver.find_element(By.CLASS_NAME, "scaffold-layout__list")
        scroll_origin = ScrollOrigin.from_element(section)
        ActionChains(self.chrome_driver).scroll_from_origin(scroll_origin, 0, 4000).perform()
        time.sleep(2)

        jobs_posting = self.chrome_driver.find_elements(By.CLASS_NAME, value="job-card-container")

        for jobs in jobs_posting:
            jobs.click()
            try:
                time.sleep(3)
                self.chrome_driver.find_element(By.CSS_SELECTOR, value="button.jobs-save-button").click()
                time.sleep(3)

                follow_section = self.chrome_driver.find_element(By.CLASS_NAME, value="scaffold-layout__detail")
                scroll_origin = ScrollOrigin.from_element(follow_section)
                ActionChains(self.chrome_driver).scroll_from_origin(scroll_origin, 0, 12000).perform()
                time.sleep(3)
                try:
                    self.chrome_driver.find_element(By.CLASS_NAME, value="follow").click()
                    time.sleep(3)
                except NoSuchElementException:
                    pass

            except NoSuchElementException:
                pass

