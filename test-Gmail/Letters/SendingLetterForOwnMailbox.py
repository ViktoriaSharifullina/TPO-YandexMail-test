import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
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
    # log in to an authorised account
    driver.get(url=url)
    wait = WebDriverWait(driver, 40)
    button_email = driver.find_element("xpath",
                                       '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button')
    button_email.click()
    email_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')))

    buttonNext = driver.find_element("xpath",
                                     '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button')
    slow_typing(email_input, email)
    buttonNext.click()
    password_input = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')))
    slow_typing(password_input, password)
    buttonLogin = driver.find_element("xpath",
                                      '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
    buttonLogin.click()

    buttonWrite = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/nav/div[2]/div/div/div/a')))

    # sending an email
    buttonWrite.click()
    inputWhom = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                               "/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div")))
    slow_typing(inputWhom, email)
    inputWhom.send_keys(Keys.RETURN)
    inputTheme = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                              '/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/div/div/input')))
    slow_typing(inputTheme, "Приветствие")
    inputTheme.send_keys(Keys.RETURN)
    inputMsg = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                            '/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div/div')))
    slow_typing(inputMsg, "Привет, как дела?")
    inputMsg.send_keys(Keys.RETURN)
    buttonSend = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                            '/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button')))
    buttonSend.click()
    done = wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[16]/div/div[2]/div[1]/span')))
    if done:
        print("SendingLetterForOwnMailbox test is OK!")
    else:
        print("SendingLetterForOwnMailbox test is FAILED!")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
