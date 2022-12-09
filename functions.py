import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def find_by_xpath(wait, xpath):
    return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0, 0.3))


def send_keys(element):
    return element.send_keys(Keys.RETURN)


def find_by_xpath_web_driver(driver, xpath):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
