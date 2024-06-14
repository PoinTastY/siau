import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)

nrcs = [ "204951", "209847", "209850", "206639", "204868"]

driver.get("https://siiauescolar.siiau.udg.mx/wal/sfpregw.inicio?pidmp=1406235&majrp=ICOM")


def wait_for_injection():
    while True:
        try:
            driver.find_element_by_name("p_matricula").send_keys("204951")
            inject_nrc(nrcs)

            break
        except selenium.common.exceptions.NoSuchElementException:
            time.sleep(.5)

def inject_nrc(nrcs):
    while True:
        try:
            for nrc in nrcs:
                driver.find_element_by_name("p_nrc").send_keys(nrc)
                driver.find_element_by_name("p_agregar").click()
        except selenium.common.exceptions.NoSuchElementException:
            break

driver.quit()