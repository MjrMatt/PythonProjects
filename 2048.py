#!python3
#2048.py
#online "2048" game simple bot
#once it gets to score 256 it let'syou cotinue to play

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

scoreElem = browser.find_element_by_class_name('score-container')
score = scoreElem.text
htmlElem = browser.find_element_by_tag_name('html')

htmlElem.send_keys(Keys.UP)
htmlElem.send_keys(Keys.UP)
moves = 0

while True:
    htmlElem.send_keys(Keys.UP)
    time.sleep(0.05)
    if score == scoreElem.text:
        htmlElem.send_keys(Keys.LEFT)
        time.sleep(0.05)
        if score == scoreElem.text:
            htmlElem.send_keys(Keys.RIGHT)
            htmlElem.send_keys(Keys.UP)
            htmlElem.send_keys(Keys.LEFT)
            time.sleep(0.05)
            if score == scoreElem.text:
                htmlElem.send_keys(Keys.DOWN)
                htmlElem.send_keys(Keys.UP)
                htmlElem.send_keys(Keys.LEFT)
                score = scoreElem.text
            score = scoreElem.text
        score = scoreElem.text
    score = scoreElem.text
    print(score)
    moves+=1
    if moves%20 == 0:
        buttonElem = browser.find_element_by_class_name('retry-button')
        if buttonElem.is_displayed():
            buttonElem.click()
        if not len(browser.find_elements_by_class_name('tile-256'))==0:
            break
print('Now is up to you')
            
