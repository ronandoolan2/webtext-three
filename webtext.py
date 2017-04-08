from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
#driver = webdriver.Firefox()
baseurl = "https://login.three.ie/"

def send_webtext(username, password, message, number):
   xpaths = { 'usernameTxtBox' : ".//*[@id='username']",
               'passwordTxtBox' : ".//*[@id='password']",
               'submitButton' :   ".//*[@id='myAccount']/form/table/tbody/tr[3]/td[2]/input[2]"
             # 'next' : ".//*[@id='next']"
            }

   mydriver = webdriver.Firefox()
   mydriver.get(baseurl)
   mydriver.maximize_window()

   #Clear Username TextBox if already allowed "Remember Me" 
   mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

   #Write Username in Username TextBox
   mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

   #Clear Password TextBox if already allowed "Remember Me" 
   #mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

   #Write Password in password TextBox
   #mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

   #Click Login button
   #mydriver.find_element_by_xpath(xpaths['next']).click()

   #import time
   #time.sleep(5)
   mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

   #Write Password in password TextBox
   mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)


   mydriver.find_element_by_xpath(xpaths['submitButton']).click()

   time.sleep(5)
   mydriver.find_element_by_xpath(".//*[@id='my-3-usefulLinks-desktop']/div[2]/div/ul[1]/li[4]/a").click()
   time.sleep(5)
   mydriver.switch_to_frame(mydriver.find_element_by_xpath("//frame"))
   mydriver.find_element_by_xpath(".//*[@id='txtA_SMSMessage']").send_keys(message)
   #mydriver.switch_to_frame(mydriver.find_element_by_xpath("//frame"))
   time.sleep(2)
   mydriver.find_element_by_xpath(".//*[@id='div_RecipientInput']").click()
   time.sleep(1)
   mydriver.find_element_by_xpath(".//*[@id='div_RecipientInput']").send_keys(number)

   mydriver.find_element_by_xpath("//*[@id='imgSendYourText']").click()
