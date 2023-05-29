import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tabulate import tabulate
import threading

# Otwarcie przeglądarki
options = webdriver.ChromeOptions()
options.add_argument('--headless')


def Scrapper(driver):
    driver.get('https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW')
    time.sleep(2)

    Data = []

    for i in range(30000, 99999):

        print(Data)
        # Pętla numerów KW
        try:
            kodWydzialu = driver.find_element(By.ID, "kodWydzialuInput")
            kodWydzialu.send_keys("BI1B")
        except:
            driver.get('https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW')
            time.sleep(3)
            kodWydzialu = driver.find_element(By.ID, "kodWydzialuInput")
            kodWydzialu.send_keys("BI1B")


        iAsString = str(i)
        Number = iAsString.rjust(7, '0') + "6"
        print(Number)
        numerKsiegiWieczystej = driver.find_element(By.ID, "numerKsiegiWieczystej")
        numerKsiegiWieczystej.clear()
        time.sleep(0.25)
        numerKsiegiWieczystej.send_keys(Number)

        cyfraKontrolna = driver.find_element(By.ID, "cyfraKontrolna")
        cyfraKontrolna.send_keys(0)

        wyszukaj = driver.find_element(By.ID, "wyszukaj")
        wyszukaj.click()

        delay = 3

        try:
            isReady = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'powrotDoKryterii')))
            try:
                workingCheck = driver.find_elements(By.TAG_NAME, 'p')
                Data.append(workingCheck[2].text + " - " + str(Number))
                time.sleep(0.5)
                driver.back()
                continue
            except:
                time.sleep(0.25)
                driver.back()
                continue
        except:
            continue

    # file = open('Wyniki.txt', 'a')
    # file.write(tabulate(Data))

for i in range(6):
    ScrapThread = threading.Thread(target=Scrapper, args=uc.Chrome(options=options))
    ScrapThread.start()