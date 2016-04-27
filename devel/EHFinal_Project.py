#Elise Harper
#Final Project

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

print('Hello! Please wait while I open Firefox.')

browser = webdriver.Firefox()   #designates Firefox as the browser
browser.get('http://www.google.com/')   #Opens the browser to Google

search = browser.find_element_by_name('q')
search.send_keys("fox 35 news instagram") #phrase searched for on Google
search.send_keys(Keys.RETURN) #Hits return after the text is entered in the search bar
time.sleep(5)  #Waits for 5 seconds so you can see the results

browser.find_element_by_xpath('//a[starts-with(@href, "https://www.instagram.com/fox35news")]').click()  #Looks for the instagram page amongst the search results and clicks it
time.sleep(5)  #Let's the page load completely

browser.save_screenshot('screenshot_photos.png')  #Saves a screenshot of the Instagram page to the current working directory
browser.quit()    #Closes the browser so that you can see the Python shell

print('Your screenshot has been saved to the current working directory on your computer')
print('Check it out!')




