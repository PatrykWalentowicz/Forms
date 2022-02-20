from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# DATA FOR TEST
WEB = 'https://app.bluealert.pl/ba/form/formularz-testowy'
NAME = 'Jan'
LAST_NAME = 'Testowy'
MAIL = 'jantestowy@go.eu'
PHONE = '516516516'
PESEL = '18091927207'
ID = 'MYS476517'
BIRTHDATE = '1985-05-16'

def openWeb(web):
    '''Get web page to test'''
    driver.get(web)

def clickNextPage():
    '''Click Next button'''
    button = driver.find_element_by_id('form_button_next')
    ActionChains(driver).move_to_element(button).click().perform()

def fillForm(name, lastName, mail, phone, pesel, id, birthdate):
    '''This feature fills all data in the form'''
    openWeb(WEB)

    findName = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_first_name')))
    findName.send_keys(name)

    fillLastName = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_last_name')))
    fillLastName.send_keys(lastName)

    fillMail = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_email')))
    fillMail.send_keys(mail)

    fillPhone = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_phone')))
    fillPhone.send_keys(phone)

    fillPESEL = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_pesel')))
    fillPESEL.send_keys(pesel)

    fillID = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_id_numer')))
    fillID.send_keys(id)

    fillBirthDate = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'id_date')))
    fillBirthDate.send_keys(birthdate)

    sleep(1)
    clickSomething = driver.find_element_by_class_name('legend').click() # click empty place on page
    sleep(1)

    clickNextPage() # click NEXT button

# Fill all empty gaps on the form
fillForm(NAME, LAST_NAME, MAIL, PHONE, PESEL, ID, BIRTHDATE)