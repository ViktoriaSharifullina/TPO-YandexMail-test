import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

url = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821%26noretpath%3D1&from=mail&origin=hostroot_homer_auth_ru"
email = "viksharifullina@yandex.ru"
password = "BodnarchuK2801"
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path="/test-Gmail/chromedriver.exe",
                          options=chrome_options)


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0, 0.3))


try:
    driver.get(url=url)
    wait = WebDriverWait(driver, 20)
    button_email = driver.find_element("xpath",
                                       '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button')
    button_email.click()
    email_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')))

    button_next = driver.find_element("xpath",
                                      '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button')
    slow_typing(email_input, email)
    button_next.click()
    password_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')))
    slow_typing(password_input, password)
    button_login = driver.find_element("xpath",
                                       '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
    button_login.click()
    topic_email = "Приветствие"
    search_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/form/div/span/input')))

    slow_typing(search_input, topic_email)
    buttonSearch = driver.find_element("xpath",
                                       '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/form/button')
    buttonSearch.click()
    answer = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                          '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/div[2]/div/main/div[7]/div[1]/div/div/div[3]/div/div[1]/div')))

    time.sleep(5)
    if answer:
        print("SearchLetters.py test is OK!")
    else:
        print("SearchLetters.py test is FAILED!")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
