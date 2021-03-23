# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
   
    server.login(mail, password)
   
    subject = 'NEWEGG SHUFFLE OPENED!'
    body = 'https://www.newegg.com/product-shuffle'
   
    msg = f"Subject: {subject}\n\n{body}"
   
    server.sendmail(mail_from, mail_to, msg)
   
    print ('Email is sent')
   
    server.quit()

# starts from here
    
mail = 'type_your_gmail'
password = 'type_your_password'
mail_from = 'type_your_gmail'
mail_to = 'type_mailaddress'

ProductURL= 'https://www.newegg.com/product-shuffle'

driver = webdriver.Chrome("C:\\Users\\PATH\\TO\\FILE\\chromedriver.exe") # NOTE THAT path to chromedriver.exe must be written accordingly.
driver.get(ProductURL) # page opens

# you will be automatically redirected to sign in page

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[1]/form/div/div[1]/div/input"
     ))).send_keys(mail) # fill input element with your gmail address
    
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div[1]/form/div/div[3]").click() # then click sing in button
    
# because of bot you will receive a sign in code to your gmail, instead of proceeding to password page.
# apply 6 digit code and click sign in button on your own.
# you need to sign-in in time stated below code line (timeout). 

timeout = 120
WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="app"]/div/section[1]/div/div[4]/p/a[2]'))) # this is just random clickable page element (Newegg Shuffle FAQ) in order to ensure page is loaded

time.sleep(3) # wait a little to load page fully

situation_change = False
while not situation_change:

    element=driver.find_element_by_xpath('//*[@id="app"]/div/section[1]/div/div[2]') #div element of text, <!-- -->NEXT SHUFFLE: TBD
    word = element.get_attribute("innerHTML") # get text
    print("word ", word)
    result=word.find('TBD') # if 'TDB' is found in given text than result is not -1
    print("result ", result)
    if(result != -1):
        print('SHUFFLE has not opened yet, check some time later') 
        time.sleep(1 * 1) # wait for a while to check again
        continue
    else:
        situation_change = True
        break

send_mail()

print('SHUFFLE opened')   
print('Script ended')     