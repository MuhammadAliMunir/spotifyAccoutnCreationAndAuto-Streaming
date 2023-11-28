from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from csv import writer
from selenium.webdriver.common.proxy import Proxy, ProxyType


# e = input("Enter the email address : ")
# p = input("Enter the password : ")
# t = input("Enter the time in SEC: ")



class bot:

    data = None
    delay = None
    def __init__(self, param1, param2):
        try:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--incognito")
            PROXY = param1['proxy']
            # print(PROXY)
            # self.chrome_options.add_argument('--proxy-server=%s' % PROXY)
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = PROXY
            prox.socks_proxy = PROXY
            prox.ssl_proxy = PROXY

            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.add_to_capabilities(capabilities)

            self.driver = webdriver.Chrome(desired_capabilities=capabilities,options=self.chrome_options)
            # self.driver = webdriver.Chrome()
            # self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.get("https://accounts.spotify.com/en/login/")
            self.data = param1
            self.delay = param2
        except :
            self.driver.close()
    def wirteCSV(self,data):
        with open('faild.csv','a',newline='') as fd:
            newFileWriter = writer(fd)
            newFileWriter.writerow([data])
            # newFileWriter.writerow([data])
    def login(self):
        try:
            wait = WebDriverWait(self.driver, self.delay)
            s = wait.until(
                EC.visibility_of_element_located((By.ID,'login-username'))
            )
            # s = self.driver.find_element_by_id("login-username")
            s.clear()
            s.send_keys(self.data['login'][0])
            s1 = wait.until(
                EC.visibility_of_element_located((By.ID,'login-password'))
            )
            # s1 = self.driver.find_element_by_id("login-password")
            s1.clear()
            s1.send_keys(self.data['login'][1])
            time.sleep(3)
            wait.until(
                EC.visibility_of_element_located((By.ID,'login-button'))
            ).click()
            # self.driver.find_element_by_id("login-button").click()
            # time.sleep(3)
            wait.until(
                EC.visibility_of_element_located((By.ID,'account-settings-link'))
            ).click()
            # self.driver.find_element_by_id("account-settings-link").click()
            wait.until(EC.url_to_be("https://www.spotify.com/int/account/overview/"))
            # self.driver.get("https://open.spotify.com/album/0C1lYODJwVYGKUXNJVLwmo")
            self.driver.get(self.data['url'])
            time.sleep(3)
            # wait.until(
            #     EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]'))
            # ).click()
            # time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]").click()
            time.sleep(1)
            minuts = round(int(self.data['time'])/60,2)
            min = str(minuts).replace('.',':')
            # print(min)
            # print(int(minuts))
            wait = WebDriverWait(self.driver, int(self.data['time'])+60)
            wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div[3]/div/div[3]/div[3]/footer/div[1]/div[2]/div/div[2]/div[1]"),min))
            wait = WebDriverWait(self.driver, self.delay)
            # wait.until(
            #     EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button'))
            # ).click()                        /html/body/div[3]/div/div[3]/div[3]/footer/div/div[1]/div/div[3]/button
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button").click()
            time.sleep(self.delay)
        except:
            self.wirteCSV(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'])
            print(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'])
            self.driver.close()
    # def like(self):
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[2]/div[2]/div[1]/div/button/div").click()
    def like(self):     ##                           /html/body/div[3]/div/div[3]/div[3]/footer/div/div[1]/div/div[3]/button
        print('like')
        heart = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[3]/footer/div/div[1]/div/div[3]/button")
        heart.click()
        # time.sleep(10)
    # def follow(self):
    #     print('follow1')
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[1]/div/div/div[2]/div/a").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/header/div/div/button[2]").click()
    #     time.sleep(5)
    #     self.driver.quit()
    def follow(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div[5]/div/a").click()
        wait = WebDriverWait(self.driver, self.delay)
        button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[2]")))
        button.click()

    # login()
    # like()
    # follow()