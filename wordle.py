import schedule
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
username = "Username" 
password = "Password"
wordlelist = []
file = open('words.txt', 'r')
text = file.read()
wordlelist = text.split()
global  wordleday
wordleday = input("Wordle #: ");
print("STARTED!!!!")
def send_answer():
    print("It's time!")
    global wordleday
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get("Link to Google Chat Space")
    time.sleep(2)
    driver.find_element_by_id("identifierId").send_keys(username, Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(password, Keys.ENTER)
    time.sleep(5)
    driver.implicitly_wait(5)
    driver.get("Google Chat Space")
    time.sleep(3.5)
    message = ("The wordle for today is " +  wordlelist[wordleday] + "!")
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(2)
    print(wordlelist[wordleday])
    driver.quit()
    wordleday += 1

schedule.every().day.at("08:15").do(send_answer)

while True:
    schedule.run_pending()
    time.sleep(1)
