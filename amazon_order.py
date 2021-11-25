# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:09:03 2021

@author: ASAID.AKBULUT
"""

import selenium
from selenium import webdriver
import pywhatkit as kit
import time
import os
import smtplib

ProductURL= 'https://www.amazon.com/dp/B08YKCRB74/?coliid=I36FBELUXR7YP9&colid=2AQE0FKI4D6DJ&psc=0&ref_=lv_vv_lig_dp_it'


driver = webdriver.Chrome("C:\\Users\\asaid.akbulut\\Desktop\\kindamessy\\python mess\\chromedriver_win32\\chromedriver.exe")
driver.get(ProductURL)
"""driver.maximize_window()"""

def place_order():
    driver.find_element_by_id("buy-now-button").click()
    """driver.close()"""
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('asaidakbulut@gmail.com', 'xxxpasswordxxx')
    
    subject = 'pyton amazon'
    body = 'https://www.amazon.com/dp/B08YKCRB74/?coliid=I36FBELUXR7YP9&colid=2AQE0FKI4D6DJ&psc=0&ref_=lv_vv_lig_dp_it'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('asaidakbulut@gmail.com', 'asaidakbulut@gmail.com', msg)
    
    print ('Email is sent')
    
    server.quit()
    
while(True):
    """if (driver.find_element_by_id("buy-now-button")==True)"""
    place_order()
    send_mail()
    """kit.sendwhatmsg("+905452047569","hello said")"""
    """os.system("taskkill /im chrome.exe /f")"""

