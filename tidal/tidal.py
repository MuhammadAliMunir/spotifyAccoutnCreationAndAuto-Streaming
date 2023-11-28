from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import options


e = input("Enter the email address : ")
to = input("Press enter after recaptacha")
p = input("Enter the password : ")
t = input("Enter the time in SEC: ")



options = Options()
options.add_extension('hola.crx')
driver = webdriver.Chrome(options= options)
driver.get("https://login.tidal.com/authorize?appMode=WEB&client_id=CzET4vdadNUFQ5JU&client_unique_key=14ece4d6-e789-43dc-b5ec-7b7e8af5ff56&code_challenge=kNYiZpLPAPUNnzc3pqtoGlRdyhlkYX-k-3UJu6EMBwg&code_challenge_method=S256&lang=en&redirect_uri=https%3A%2F%2Flisten.tidal.com%2Flogin%2Fauth&response_type=code&restrictSignup=true&scope=r_usr%20w_usr&state=TIDAL_1586991537465_MTEyLDU1LDU5LDE5MiwyMjcsOTksMjIxLDExLDIxMyw1MywyMjMsMjM2LDI1NCwyNDYsMTE0LDIxMyw2NSwzNyw5OCwxNDQsMTU3LDIzNCwyMjMsMjQsMTQyLDE5MCwyMTEsNzIsMTEyLDEyMSwxMTQsMjAx&utm_banner=na&utm_campaign=na&utm_content=left_menu&utm_medium=web_player&utm_source=tidal")

def login():
    wait = WebDriverWait(driver, 12)
    E = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div/div/div/div[1]/div/form/div/input")))
    E.send_keys(e)
    time.sleep(1)
    Button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div/div[1]/div/form/button/div/div")
    Button.click()
    time.sleep(to)
    E2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[3]/input")
    E2.send_keys(p)
    login = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/form/button/div")))
    login.click()
    time.sleep(2)
    wait.until(EC.url_to_be("https://listen.tidal.com/"))
    driver.get("https://listen.tidal.com/artist/4761957")
    time.sleep(2)
    playbutton = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div[2]/main/div[1]/div[2]/div/div[1]/span/div/div/header/div[2]/div[2]/button[1]/span")
    playbutton.click()
    minuts = round(int(t)/60,2)
    min = str(minuts).replace('.',':')
    print(min)
    print(int(minuts))
    wait = WebDriverWait(driver, int(t)+60)
    wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]"),min))
    wait = WebDriverWait(driver, 12)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button[3]/svg[2]").click()
    time.sleep(10)
    follow()


def follow():
    time.sleep(3)
    heart = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div[2]/main/div[1]/div[2]/div/div[1]/span/div/div/header/div[2]/div[2]/button[3]/i")
    heart.click()


login()

