import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# url = "https://accounts.google.com/v3/signin/identifier?dsh=S1728490719%3A1670309494363551&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAvHjI6CD-IrLY3hotEvjz_2UvpnrJxVUt-0RRcY1dCemTzH53YeNhvBfDheWtmirP7gAFia3Q"
from selenium.webdriver.support.wait import WebDriverWait

url = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821%26noretpath%3D1&from=mail&origin=hostroot_homer_auth_ru"
email = "viksharifullina@yandex.ru"
password = "BodnarchuK2801"
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path="C:/Users/Админ/PycharmProjects/test-Gmail/test-Gmail/chromedriver.exe",
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

    buttonAccount = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                 '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[3]/div/div/a[1]/div')))
    buttonAccount.click()
    buttonLogOut = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[3]/div/div/div/ul/ul/li[6]/a/span')))
    buttonLogOut.click()

    button_LogIn = wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div[2]/button')))

    if button_LogIn:
        print("LogOutAuthorisedUser test is OK!")

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
