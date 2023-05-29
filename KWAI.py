import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading


# Function to run the program for a given i range
def run_program(start, end, driver_number):
    try:
        # List of driver paths
        driver_paths = [
            "C:\\Users\\ayoxe\\appdata\\roaming\\undetected_chromedriver\\undetected1\\chromedriver.exe",
            "C:\\Users\\ayoxe\\appdata\\roaming\\undetected_chromedriver\\undetected2\\chromedriver.exe"
        ]

        # Loop to open multiple drivers
        for i, driver_path in enumerate(driver_paths):
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-extensions')
            driver = uc.Chrome(options=options, driver_executable_path=driver_path)
            driver.get('https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW')
            time.sleep(2)
            print(f"Driver {i + 1} opened successfully.")

        Data = []

        for i in range(start, end):
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
                isReady = WebDriverWait(driver, delay).until(
                    EC.presence_of_element_located((By.ID, 'powrotDoKryterii')))
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
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()


# Define the i ranges for each driver
driver1_start = 30000
driver1_end = 40000

driver2_start = 40000
driver2_end = 50000


# Create threads for each driver
thread1 = threading.Thread(target=run_program, args=(driver1_start, driver1_end, 1))
thread2 = threading.Thread(target=run_program, args=(driver2_start, driver2_end, 2))

# Start the threads
thread1.start()
thread2.start()

