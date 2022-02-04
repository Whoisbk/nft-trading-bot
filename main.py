from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3
from time import sleep
import smtplib

#https://sites.google.com/chromium.org/driver/  THIS IS THE LINK TO DOWNLOAD THE WEBDRIVERS FOR YOUR CHROME BROWSER

PATH = "C:\Program Files (x86)\geckodriver.exe"#GET THE PATH TO THE WEBDRIVER YOU JUST DOWNLOADED
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://opensea.io/")#website path you want to go to

search = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/nav/div[2]/div/div/div/input")
search.send_keys("The Doge pound")
search.send_keys(Keys.RETURN)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#def email(message):#send message from the senders email to the reciever
#    server = smtplib.SMTP('smtp.gmail.com',587)
#    server.starttls()
 #   server.login("botshelolaka91@gmail.com","bk13@future")
#  server.sendmail("botshelolaka91@gmail.com","beekayhuncho@gmail.com",message)

try:
        num_owners = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/main/div/div/div[3]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div/a/div/div[2]/div[2]/div[1]/div/span/div"))
        )

        tot_items = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/main/div/div/div[3]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div/a/div/div[2]/div[1]/div[1]/div/span/div"))
        )

        floor_price = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/main/div/div/div[3]/div[1]/div[1]/div/div/div/div/div/div[3]/div/div/a/div/div[2]/div[3]/div[1]/div/span/div"))
        )

        speak("Num Owners:......." + num_owners.text + ".......")
        speak("Total Items:........ " + tot_items.text +"........")
        speak("Floor Price:........ " + floor_price.text+"Etherium..........")
        
        floor_price_list = ["3.58"]
        floor_price_list.append(floor_price.text)
    
                
        def compare(floor_price_list):
            if(floor_price_list[-1] < floor_price_list[-2]):
                return True
            elif(floor_price_list[-1] > floor_price_list[-2]) :
                return False
            else:
                return 0
            

        flag = compare(floor_price_list)
       
        if flag :
            decrease = floor_price[-1] - floor_price[-2]
            msg = f'The floor price has went down by {decrease}'
            speak(msg)
            email(msg)
            #email(msg)
        elif flag != True:
            increase = floor_price[-2] - floor_price[-1]
            msg = f'The floor price has went up by {increase}'
            speak(msg)
            email(msg)
        else:
            msg = f'The floor price has not changed'
            speak(msg)
            email(msg)

        driver.back()

        explore = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Explore"))
        )

        explore.click()

        #Trending
        
        no1_trend = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/main/div/div[2]/div/div/div[1]/div/a/div[2]/div[2]/div"))
        )

        no2_trend = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/div/a/div[2]/div[2]/div[1]"))
        )

        no3_trend = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/main/div/div[2]/div/div/div[3]/div/a/div[2]/div[2]/div"))
        )

        verification = "/html/body/div[1]/div/main/div/div[2]/div/div/div[2]/div/a/div[2]/div[2]/div[2]/div/svg/path[1]"
        speak("Top 3 Trending NFT....")
        speak("Number 1 Trending NFT:..."+ no1_trend.text +"....")
        speak("Number 2 Trending NFT:..."+ no2_trend.text +"....")
        speak("Number 3 Trending NFT:..."+ no3_trend.text +"....")

        #names = driver.find_elements_by_class_name("Blockreact__Block-sc-1xf18x6-0 CarouselCardreact__Container-sc-152cap8-0 dBFmez eyjpLW")
        
except:
    driver.quit()




time.sleep(200)
driver.quit()