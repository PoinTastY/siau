import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

nrcs = [ "204951", "209847", "209850", "206639", "204868","209754", "210931", "210933", "209852", "210926"]

driver.get("https://siiauescolar.siiau.udg.mx/wal/sfpregw.inicio?pidmp=1406235&majrp=ICOM")


def wait_for_injection():
    while True:
        try:
            driver.find_element(By.XPATH, "/html/body/li[6]/center/form/table/tbody/tr[2]/td[1]/input")
            driver.implicitly_wait(1)
            if(inject_nrc()):
                break

        except selenium.common.exceptions.NoSuchElementException:
            pyautogui.press('f5')
            

def inject_nrc():
    while True:
        try:
            index = 0
            for nrc in nrcs:
                element = driver.find_element(By.XPATH, f"/html/body/li[6]/center/form/table/tbody/tr[2]/td[{index + 1}]/input")
                element.send_keys(nrc)
                index += 1
            submit_button = driver.find_element(By.XPATH, "/html/body/li[6]/center/form/input[7]")
            submit_button.click()
            time.sleep(1)
            clear_button = driver.find_element(By.XPATH, "/html/body/li[7]/center/table[2]/tbody/tr/td[1]/input")
            clear_button.click()
            time.sleep(.5)
            if(validate_injection()):
                print("Inyección exitosa")
                return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

def validate_injection():
    while True:
        try:
            tabla = driver.find_element(By.XPATH, "/html/body/li[7]/center/table[1]")
            filas = tabla.find_elements(By.TAG_NAME, "tr")
            for fila in filas:
                celdas = fila.find_elements(By.TAG_NAME, "td")
                for celda in celdas:
                    if(celda.text in nrcs):
                        nrcs.remove(celda.text)
            if(len(filas) >= 6):
                return True
            else:
                return False
        except:
            return False

wait_for_injection()

driver.quit()