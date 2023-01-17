import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_current_timetable():

    s = Service('C:/webdrivers/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    url = 'https://getmobile.eurotunnel3.com/front/'
    browser.get(url)

    time.sleep(6)

    user_field = browser.find_element(By.ID, "i0116")
    user_field.send_keys("")

    # Récupérer la valeur saisie dans le champ
    email = user_field.get_attribute("value")

    # Vérifier si la valeur ressemble à une adresse email valide
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    match = re.search(pattern, email)

    if match:
        print("L'adresse email saisie est valide.")
    else:
        print("L'adresse email saisie n'est pas valide.")

    btn_next = browser.find_element(By.ID, "idSIButton9")
    btn_next.click()

    time.sleep(6)

    passwd_field = browser.find_element("name", "passwd")
    passwd_field.send_keys("")

    btn_auth = browser.find_element(By.ID, "idSIButton9")
    btn_auth.click()

    time.sleep(60)
    browser.quit()
