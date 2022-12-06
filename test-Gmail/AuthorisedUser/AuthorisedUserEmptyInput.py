import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

url = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821%26noretpath%3D1&from=mail&origin=hostroot_homer_auth_ru"
phone = ""
email = ""

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
    button_phone = driver.find_element("xpath",
                                       '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button')
    button_phone.click()
    phone_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/span/input')))

    buttonNext = driver.find_element("xpath",
                                     '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button')
    slow_typing(phone_input, phone)
    buttonNext.click()

    msgError = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                            '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]')))
    if  msgError:
        print("AuthorisedUserEmptyInput.py(phone): passed")
    else:
        print("AuthorisedUserEmptyInput.py(phone): failed")

    # EmptyLogin
    button_email = driver.find_element("xpath",
                                       '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button')
    button_email.click()
    email_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')))

    buttonNext1 = driver.find_element("xpath",
                                      '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button')
    slow_typing(email_input, email)
    buttonNext1.click()

    msgError1 = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                            '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/div')))
    if msgError1:
        print("AuthorisedUserEmptyInput.py(login): passed")
    else:
        print("AuthorisedUserEmptyInput.py(login): failed")


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
