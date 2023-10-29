from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser_timeout = time.time() + 60 * 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

while True:
    upgrades_available = []
    upgrade_costs = []

    if time.time() > browser_timeout:
        break

    upgrades_store = chrome_driver.find_elements(By.CSS_SELECTOR, "#store div")
    money = int(chrome_driver.find_element(By.ID, value="money").text)

    for upgrades in upgrades_store:
        if upgrades.get_attribute(name="class") != "grayed":
            upgrades_available.append(upgrades)
            try:
                upgrade_costs.append(int(upgrades.text.split("\n")[0].split("-")[1].strip()))
            except IndexError:
                pass

    if len(upgrade_costs) != 0:
        best_upgrade = max(upgrade_costs)
        best_upgrade_index = upgrade_costs.index(best_upgrade)

        if money >= best_upgrade:
            upgrades_available[best_upgrade_index].click()

    cookie_clicker = chrome_driver.find_element(By.ID, value="cookie")
    cookie_clicker.click()

cookie_seconds = chrome_driver.find_element(By.ID, value="cps")
print(cookie_seconds.text)

chrome_driver.quit()
