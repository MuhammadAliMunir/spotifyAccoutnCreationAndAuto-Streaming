from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from csv import writer
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType

class bot:

    data = None
    delay = None
    def __init__(self, param1, param2):
        try:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--incognito")
            PROXY = param1['proxy']
            self.chrome_options.add_argument('--proxy-server=%s' % PROXY)
            # self.driver = webdriver.Chrome(options=self.chrome_options)
            prox = Proxy()
            prox.proxy_type = ProxyType.MANUAL
            prox.http_proxy = PROXY
            prox.socks_proxy = PROXY
            prox.ssl_proxy = PROXY

            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.add_to_capabilities(capabilities)
            self.driver = webdriver.Chrome(desired_capabilities=capabilities,options=self.chrome_options)

            # self.driver = webdriver.Chrome(desired_capabilities=capabilities)
            self.driver.get("https://accounts.spotify.com/en/login/")
            self.wait = WebDriverWait(self.driver, param2)
            self.data = param1
            self.delay = param2
        except:
            self.driver.close()
    def song(self):
        self.driver.get(self.data['url'])
        # self.driver.get("https://open.spotify.com/artist/1ZChN8G1Y7CJ0TXbrvblwS")
        time.sleep(3)
        i = 1 
        while i > 0:
            try:
                self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div/section[1]/div/section/section/ol/div[ "+ str(i) + "]/div/li/div[1]/div[2]").click()
                time.sleep(3)               
                minuts = round(int(self.data['time'])/60,2)
                min = str(minuts).replace('.',':')
                print(min)
                print(int(minuts))
                wait = WebDriverWait(self.driver, int(self.data['time'])+60)
                wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div[3]/div/div[3]/div[3]/footer/div[1]/div[2]/div/div[2]/div[1]"),min))
                wait = WebDriverWait(self.driver, 12)
                self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button").click()
                time.sleep(3)
                i += 1
            except:
                print('')

    def like(self):
        heart = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[3]/footer/div/div[1]/div/div[3]/button")
        heart.click()

    def follow(self):
        time.sleep(3)
        fol = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[2]")
        fol.click()

    def wirteCSV(self,data):
        with open('faild.csv','a',newline='') as fd:
            newFileWriter = writer(fd)
            newFileWriter.writerow([data])
            # newFileWriter.writerow([data])

    def play(self):
        try:
            s = self.driver.find_element_by_id("login-username")
            s.send_keys(self.data['login'][0])
            s1 = self.driver.find_element_by_id("login-password")
            s1.send_keys(self.data['login'][1])
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button").click()
            time.sleep(4)
            element = self.wait.until(EC.element_to_be_clickable((By.ID, 'account-settings-link')))  
            element.click()
            self.wait.until(EC.url_to_be("https://www.spotify.com/int/account/overview/"))
        
        except NoSuchElementException:
            # print(e)
            self.wirteCSV(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'][0]+' , '+self.data['proxy'][1])
            print(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'][0]+' , '+self.data['proxy'][1])
            self.driver.close()
        except TimeoutException:
            # print(e)
            self.wirteCSV(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'][0]+' , '+self.data['proxy'][1])
            print(self.data['login'][0]+' , '+self.data['login'][1]+' ; '+self.data['proxy'][0]+' , '+self.data['proxy'][1])
            self.driver.close()
    #     song()  
    #     like()
    #     follow()
    # play()
