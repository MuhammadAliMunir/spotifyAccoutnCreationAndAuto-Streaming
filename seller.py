from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.actions
import time
import os
from selenium.webdriver.common.by import By 


U = "sq787954@gmail.com"
P = "Salu@12345??"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 18)
def login():
    driver.get("https://app.sellerlegend.com/login")
    email = wait.until(EC.visibility_of_element_located((By.ID,"email")))
    email.send_keys(U)
    pas = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div[2]/div/form/div[2]/div/input")))
    pas.send_keys(P)
    button = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/div/form/button')))
    button.click()
    wait.until(EC.url_to_be("https://app.sellerlegend.com/home"))
    driver.get("https://app.sellerlegend.com/products/index")
    
def search():
    clicksearch = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[1]/div[2]/a[1]')))
    clicksearch.click()
    enter = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/input')))
    enter.send_keys("B000BRV9RA")
    time.sleep(2)
    No = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/span'))).text 
    No1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[10]/span'))).text 
    if No:
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div/button')))
        dropdown.click()
        time.sleep(2)
        entergoods = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div/ul/li[1]/a')))
        entergoods.click()
    else:
        print("Active button not found")
    
    if No1:
        dropdown1 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[1]/div/div/button')))
        dropdown1.click()
        time.sleep(2)
        entergoods1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[6]/div/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[1]/div/div/button')))
        entergoods1.click()
    else:
        print("Active button not found")
        
login()
search()