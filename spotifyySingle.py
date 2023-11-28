from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from csv import writer
from selenium.webdriver.common.proxy import Proxy, ProxyType
import zipfile
import os

# e = input("Enter the email address : ")
# p = input("Enter the password : ")
# t = input("Enter the time in SEC: ")



class bot:

    data = None
    delay = None
    def __init__(self, param1, param2):
        # try:

            self.chrome_options = webdriver.ChromeOptions()
            # self.chrome_options.add_argument("--incognito")
            PROXY = param1['proxy']

            # PROXY = PROXY.split(':')
            # # print(PROXY)
            # # exit()
            # PROXY_HOST = PROXY[0]  # rotating proxy
            # PROXY_PORT = PROXY[1]
            # PROXY_USER = '471778020'
            # PROXY_PASS = 'c12ea3'

            # # print(PROXY_HOST,PROXY_PORT,PROXY_USER,PROXY_PASS)
            # # exit()
            # manifest_json = """
            # {
            #     "version": "1.0.0",
            #     "manifest_version": 2,
            #     "name": "Chrome Proxy",
            #     "permissions": [
            #         "proxy",
            #         "tabs",
            #         "unlimitedStorage",
            #         "storage",
            #         "<all_urls>",
            #         "webRequest",
            #         "webRequestBlocking"
            #     ],
            #     "background": {
            #         "scripts": ["background.js"]
            #     },
            #     "minimum_chrome_version":"22.0.0"
            # }
            # """

            # background_js = """
            # var config = {
            #         mode: "fixed_servers",
            #         rules: {
            #         singleProxy: {
            #             scheme: "http",
            #             host: "%s",
            #             port: parseInt(%s)
            #         },
            #         bypassList: ["localhost"]
            #         }
            #     };

            # chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            # function callbackFn(details) {
            #     return {
            #         authCredentials: {
            #             username: "%s",
            #             password: "%s"
            #         }
            #     };
            # }

            # chrome.webRequest.onAuthRequired.addListener(
            #             callbackFn,
            #             {urls: ["<all_urls>"]},
            #             ['blocking']
            # );
            # """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
            # pluginfile = 'proxy_auth_plugin.zip'

            # with zipfile.ZipFile(pluginfile, 'w') as zp:
            #     zp.writestr("manifest.json", manifest_json)
            #     zp.writestr("background.js", background_js)
            # self.chrome_options.add_extension(pluginfile)

            print(PROXY)
            # PROXY = "165.138.4.41:8080"

            # chrome_options = WebDriverWait.ChromeOptions()
            self.chrome_options.add_argument('--proxy-server=%s' % PROXY)

            # chrome = webdriver.Chrome(chrome_options=self.chrome_options)
            # chrome.get("https://www.google.com")
            # self.driver = webdriver.Chrome(
            #     os.path.join(path, 'chromedriver'),
            #     chrome_options=chrome_options)

            # # self.driver = webdriver.Chrome(desired_capabilities=capabilities,options=self.chrome_options)
            # self.driver = webdriver.Chrome()
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.get("https://accounts.spotify.com/en/login/")
            # time.sleep(500)
            self.data = param1
            self.delay = param2
            print(self.data)
        # except :
        #     print('abc')
        #     # self.driver.close()
    def wirteCSV(self,data):
        with open('faild.csv','a',newline='') as fd:
            newFileWriter = writer(fd)
            newFileWriter.writerow([data])
            # newFileWriter.writerow([data])
    def login(self):
        # try:
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
            # time.sleep(300)
            wait.until(
                EC.visibility_of_element_located((By.ID,'account-settings-link'))
            ).click()
            # self.driver.find_element_by_id("account-settings-link").click()
            time.sleep(5)
            # wait.until(EC.url_to_be("https://www.spotify.com/us/account/overview/"))
            # self.driver.get("https://open.spotify.com/album/0C1lYODJwVYGKUXNJVLwmo")
            print(self.data['url'])
            self.driver.get(self.data['url'])
            time.sleep(3)
            # wait.until(
            #     EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]'))
            # ).click()
            # time.sleep(2)
            # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]").click()
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
        # except:
        #     self.wirteCSV(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'])
        #     print(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'])
        #     self.driver.close()
