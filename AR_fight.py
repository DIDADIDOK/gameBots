from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from multiprocessing import Pool
import time
import json

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options = chrome_options)

with open("AR_fight.txt", "r") as file:
    data = json.load(file)
    count = data["count"]

def main(Login, Password, Acc):
    ####LOGIN####
    print("Login in WAX account...")
    driver.maximize_window()
    driver.get("https://all-access.wax.io/")
    time.sleep(5)
    login = driver.find_element(By.XPATH, "//input[@name='userName']")
    login.clear()
    login.send_keys(Login)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.clear()
    password.send_keys(Password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    #####BLCKS#####
    driver.get("https://wax.bloks.io/account/ancientrealm?loadContract=true&tab=Actions&account=ancientrealm&scope=ancientrealm&limit=100&action=fight")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Login']"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Cloud Wallet']"))).click()
    time.sleep(5)

    ####MINERS####
    miner = driver.find_element_by_xpath("//input[@placeholder='Enter account name...']")
    miner.clear()
    miner.send_keys(Acc)
    miner1 = driver.find_element(By.XPATH, "//input[@placeholder='Enter number...']")
    miner1.clear()
    miner1.send_keys("15")
    timer = 1
    while timer < 20:
        timer += 1
        driver.find_element_by_xpath("//button[text()=' Submit Transaction ']").click()
        print("!!!Mined!!!")
        current_datetime = datetime.now()
        print(current_datetime)
        time.sleep(10820)
        if timer > 19:
            timer = 1;

if __name__ == "__main__":
    p = Pool(processes=count)
    p.starmap(main, data[["accs"][0]])