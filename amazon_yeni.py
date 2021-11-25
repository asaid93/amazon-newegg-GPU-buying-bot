# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:51:05 2021

@author: ASAID.AKBULUT
"""

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import smtplib


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
   
    server.login('asaidakbulut@gmail.com', 'xxxpasswordxxx')
   
    subject = 'pyton amazon'
    body = 'https://www.newegg.com/black-msi-gl-series-gl75-10sfk-029-gaming-entertainment/p/N82E16834155401?Item=N82E16834155401'
   
    msg = f"Subject: {subject}\n\n{body}"
   
    server.sendmail('asaidakbulut@gmail.com', 'asaidakbulut@gmail.com', msg)
   
    print ('Email is sent')
   
    server.quit()
   
def add_to_cart():
    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ProductBuy"]/div/div[2]/button'))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[text()="No, thanks"]'))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[text()="View Cart & Checkout"]'))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div/div/div[1]/button"))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[text()=" Secure Checkout "]'))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]"))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div/div[3]/button[2]'))).click() 
    driver.execute_script("window.scrollTo(0, 200)")
    """sayfayi asagi dogru scrolldown yapti cunku element gozukmuyordu"""
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue to delivery"]'))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button"))).click()
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/label/div[4]/input"))).send_keys('123')



ProductURL= 'https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-Tech-2-9-Slot/dp/B08J6F174Z?ref_=ast_sto_dp'

driver = webdriver.Chrome("C:\\Users\\asaid.akbulut\\Desktop\\kindamessy\\python mess\\chromedriver_win32\\chromedriver.exe")
driver.get(ProductURL)

"""asagidaki bes komut: acilan iki kucuk pencereyi kapatıyor. sag ustten sign-in oluyor. maili yazıyor. sign-in e basıyor."""
WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div/div/a"))).click()
WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[4]/div[1]/div/a"))).click()
WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/header/div[1]/div[4]/div[1]/div[1]/a"))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[1]/form/div/div[1]/div/input")
        )).send_keys('asaidakbulut@gmail.com')
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div[1]/form/div/div[3]").click()
"""sonra biz manuel olarak maile gelen kodu girip. sign-in e basıyoruz."""

"""sonra asagida while dongusuyle """
time.sleep(10)
Buton_found = False

while not Buton_found:

    x = check_exists_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')

    if x == True:
        print("dongudeki", Buton_found, "\n", "tus bulundu", x)
        Buton_found = True
        print("dongudeki", Buton_found, "\n", "tus bulundu", x)
        break
    else:
        print("dongudeki", Buton_found, "\n", "tus bulundu", x)
        continue
print("tus bulundu dongu son buldu")    

add_to_cart()
send_mail()

