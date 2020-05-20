from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pynput.keyboard import Key,Controller

browser = webdriver.Firefox()
browser.get("https://yts.mx/browse-movies")
Search = input("")
wait = WebDriverWait(driver, 5)

elem= browser.find_element_by_id("quick-search-input")
elem.click()
elem.send_keys(Search)
time.sleep(5)
elem.send_keys(Keys.ENTER)
time.sleep(5)

try:
    elem= browser.find_element_by_id("skip-ad-in-button")
    elem.click()
except:
    print("No Pop-Up here")

try:
    Knop_Plek_een  = browser.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[4]/p/a[2]").click()
except:
    try:
        Knop_plek_twee = browser.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[4]/p/a[1]").click()
    except:
        try:
            Knop_plek_drie = browser.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[4]/p/a[3]").click()
        except:
            try:
                Knop_plek_vier = browser.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[4]/p/a[4]").click()
            except:
                print("X_Paths niet gevonden")
                pass
            else:
                print("X_Path van 4 was found")
        else:
            print("X_Path van 3 was found")
    else:
        print("X_Path van 2 was found")
else:
    print("X_Path van 1 was found")

time.sleep(5)

keyboard = Controller()
keyboard.press(Key.enter)
time.sleep(3)
keyboard.press(Key.enter)
print("Your file is donwloading...")
