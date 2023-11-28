from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# e = input("Enter the email address : ")
# p = input("Enter the password : ")
# t = input("Enter the time in SEC: ")



class bot:
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://accounts.spotify.com/en/login/")
    data = None
    delay = None
    def __init__(self, param1, param2):
        self.data = param1
        self.delay = param2
    def login(self):
        wait = WebDriverWait(self.driver, self.delay)
        s = self.driver.find_element_by_id("login-username")
        s.clear()
        s.send_keys(self.data['login'][0])
        s1 = self.driver.find_element_by_id("login-password")
        s1.clear()
        s1.send_keys(self.data['login'][1])
        # time.sleep(3)
        self.driver.find_element_by_id("login-button").click()
        # time.sleep(3)
        self.driver.find_element_by_id("account-settings-link").click()
        wait.until(EC.url_to_be("https://www.spotify.com/int/account/overview/"))
        # self.driver.get("https://open.spotify.com/album/0C1lYODJwVYGKUXNJVLwmo")
        self.driver.get(self.data['url'])
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[2]/div[2]/div[1]/button").click()
        time.sleep(1)
        minuts = round(int(self.data['time'])/60,2)
        min = str(minuts).replace('.',':')
        print(min)
        print(int(minuts))
        wait = WebDriverWait(self.driver, int(self.data['time'])+60)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div[3]/div/div[3]/div[3]/footer/div[1]/div[2]/div/div[2]/div[1]"),min))
        wait = WebDriverWait(self.driver, self.delay)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button").click()
        time.sleep(self.delay)

    def like(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[2]/div[2]/div[1]/div/button/div").click()

    def follow(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[1]/div/div/div[2]/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/header/div/div/button[2]").click()
        time.sleep(5)
        self.driver.quit()

    # login()
    # like()
    # follow()