from behave import given, when, then, step
from selenium import webdriver
from functions import *

URL = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821%26noretpath%3D1&from=mail&origin=hostroot_homer_auth_ru"
EMAIL = 'mietpythontest@yandex.ru'
PASSWORD = '2323test'


@given("I'm on the login page")
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(executable_path="/test-Gmail/chromedriver.exe", options=chrome_options)
    context.driver.get(URL)


@when("I select email as login type")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button').click()


@step("I enter user's email {email}")
def step_impl(context, email):
    wait = WebDriverWait(context.driver, 40)
    email_input = find_by_xpath(wait,
                                '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')
    slow_typing(email_input, email)


@step("I click on first button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button').click()


@step('I enter user\'s password {password}')
def step_impl(context, password):
    wait = WebDriverWait(context.driver, 40)
    password_input = find_by_xpath(wait,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')
    slow_typing(password_input, password)


@step("I click on second button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button').click()


@then("I should see user's Inbox page")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    button_write = find_by_xpath(wait,
                                 '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/nav/div[2]/div/div/div/a')

    if button_write:
        print("AuthorisedUserLogin test is OK!")

    context.driver.close()
    context.driver.quit()


@step("I enter stranger's email {email}")
def step_impl(context, email):
    wait = WebDriverWait(context.driver, 40)
    email_input = find_by_xpath(wait,
                                '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')
    slow_typing(email_input, email)


@step("I click on login button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button').click()


@then("I should see NoUserExists message")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/div')

    context.driver.close()
    context.driver.quit()


@step("I enter {something} which is not user's password")
def step_impl(context, something):
    wait = WebDriverWait(context.driver, 40)
    password_input = find_by_xpath(wait,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')
    slow_typing(password_input, something)


@then("I should see WrongPassword message")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/div')

    context.driver.close()
    context.driver.quit()


@given("I'm authenticated user on inbox page {email} {password}")
def step_impl(context, email, password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = False
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(executable_path="/test-Gmail/chromedriver.exe", options=chrome_options)
    context.driver.get(URL)
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button').click()
    email_input = find_by_xpath(wait,
                                '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')
    slow_typing(email_input, email)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button').click()
    password_input = find_by_xpath(wait,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')
    slow_typing(password_input, password)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button').click()
    find_by_xpath(wait,
                  '/html/body/div[3]/div[2]/div[7]/div/div[3]/div/nav/div[2]/div/div/div/a')


@when("I click on my profile picture")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[3]/div/div/a[1]/div').click()


@step("Click on LogOut")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[3]/div[2]/div[7]/div/div[2]/div/div/div[3]/div/div/div/ul/ul/li[6]/a/span').click()


@then("I should not see user's Inbox page")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div/div/div[1]/div[2]/button')

    context.driver.close()
    context.driver.quit()


@step("I don't enter user's email")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    email_input = find_by_xpath(wait,
                                '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/span/input')
    slow_typing(email_input, '')


@then("I should see message about empty field")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]/div')

    context.driver.close()
    context.driver.quit()


@when("I select phone as login type")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button').click()


@step("I don't enter user's phones")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    phone_input = find_by_xpath(wait,
                                '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/span/input')
    slow_typing(phone_input, '')


@then("I should see message about invalid format message")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]')

    context.driver.close()
    context.driver.quit()


@step("I enter stranger's phone {phone}")
def step_impl(context, phone):
    wait = WebDriverWait(context.driver, 40)
    email_input = find_by_xpath(wait,
                                '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/span/input')
    slow_typing(email_input, phone)


@then("I should see message about phone's format")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,
                  '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/div/div[2]')

    context.driver.close()
    context.driver.quit()