import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_ENDPOINT = ("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
                   "%22mapBounds%22%3A%7B%22north%22%3A37.8826759178948%2C%22east%22%3A-122.23248568896484%2C%22south"
                   "%22%3A37.66775178944106%2C%22west%22%3A-122.63417331103516%7D%2C%22isMapVisible%22%3Atrue%2C"
                   "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D"
                   "%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B"
                   "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue"
                   "%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba"
                   "%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B"
                   "%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%7D")

# Get the headers by Inspecting the website -> Networks -> Refresh page -> Click on one of the failed requests.
# Click on Headers to get all the headers you need to pass in the get() request to be able to access the website.
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://www.zillow.com',
    'Referer': 'https://www.zillow.com',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
}


class ZillowRentalSearch:
    def __init__(self):
        self.all_addresses = []
        self.all_links = []
        self.all_prices = []

        # Get the contents of the zillow website using requests.
        zillow_response = requests.get(url=ZILLOW_ENDPOINT, headers=headers)
        zillow_response.raise_for_status()
        zillow_content = zillow_response.text

        # Parse the content of the zillow website using BeautifulSoup.
        self.zillow_soup = BeautifulSoup(zillow_content, 'html.parser')

    def get_listings(self):
        """Creates a list of addresses, links and prices."""
        link_prefix = "https://www.zillow.com"
        all_address = self.zillow_soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
        all_anchors = self.zillow_soup.find_all(name="a", class_="property-card-link",
                                                attrs={"data-test": "property-card-link"})

        # Gets all addresses, prices and links as a list.
        for address in all_address:
            self.all_addresses.append(address.get_text())

        for anchor_index in range(0, len(all_anchors), +2):
            if all_anchors[anchor_index]['href'][0:5] == "https":
                self.all_links.append(all_anchors[anchor_index]['href'])
            else:
                self.all_links.append(f"{link_prefix}{all_anchors[anchor_index]['href']}")

        all_prices = self.zillow_soup.find_all("span", {"data-test": "property-card-price"})

        for price in all_prices:
            self.all_prices.append(price.get_text())

    def fill_form(self, url):
        """Fills the form with the data extracted as list in get_listings() function."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        chrome_driver = webdriver.Chrome(chrome_options)
        chrome_driver.maximize_window()
        entry_counter = 0

        while entry_counter < len(self.all_links):
            chrome_driver.get(url=url)
            time.sleep(3)
            chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input').send_keys(
                self.all_addresses[entry_counter])
            chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input').send_keys(
                self.all_prices[entry_counter])
            chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input').send_keys(
                self.all_links[entry_counter])
            time.sleep(2)
            chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

            entry_counter += 1
        # chrome_driver.quit()
