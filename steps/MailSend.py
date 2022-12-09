from behave import given, when, then, step
from selenium import webdriver
from functions import *




URL = "https://passport.yandex.ru/auth/welcome?retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D1002378821%26noretpath%3D1&from=mail&origin=hostroot_homer_auth_ru"


EMAIL ="mietpythontest@yandex.ru"
PASSWORD = "2323test"

@given("I'm authenticated user on inbox page")
def step_impl(context):
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
    slow_typing(email_input, EMAIL)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[4]/button').click()
    password_input = find_by_xpath(wait,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/div[1]/span/input')
    slow_typing(password_input, PASSWORD)
    find_by_xpath(wait,
                  '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button').click()


@when("I click on Write button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,context.driver,'/html/body/div[3]/div[2]/div[7]/div/div[3]/div/nav/div[2]/div/div/div/a').click()


@step("I fill Email field with user's email")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    input_whom = find_by_xpath(wait,context.driver,"/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div")
    slow_typing(input_whom, EMAIL)
    input_whom.send_keys(Keys.RETURN)


@step("I fill Subject field with {subject}")
def step_impl(context,subject):
    wait = WebDriverWait(context.driver, 40)
    inputTheme = wait.until(ec.visibility_of_element_located((By.XPATH,
                                                              '/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/div/div/input')))
    slow_typing(inputTheme, subject)
    inputTheme.send_keys(Keys.RETURN)


@step("I fill Body field with {body}")
def step_impl(context,body):
    wait = WebDriverWait(context.driver, 40)
    inputMsg = find_by_xpath(wait,context.driver,'/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div/div')
    slow_typing(inputMsg, body)
    inputMsg.send_keys(Keys.RETURN)


@step("Click Send button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    find_by_xpath(wait,context.driver,'/html/body/div[3]/div[2]/div[10]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button').click()


@then("I should see a message that the letter has been sent")
def step_impl(context):
    wait = WebDriverWait(context.driver, 40)
    done = find_by_xpath(wait,context.driver,'/html/body/div[16]/div/div[2]/div[1]/span')
    if done:
        print("SendingLetterForOwnMailbox test is OK!")
    else:
        print("SendingLetterForOwnMailbox test is FAILED!")
    context.driver.close()
    context.driver.quit()
