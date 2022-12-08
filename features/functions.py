import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def find_by_xpath(wait, driver, xpath):
    return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0, 0.3))


def sendKeys(element):
    return element.send_keys(Keys.RETURN)


