# modify these values
waittime = 4														# seconds browser waits before giving up
sleeptime = [5,15]													# random seconds range before loading next video id
headless = True														# select True if you want the browser window to be invisible (but not inaudible)

#do not modify below
from time import sleep
import json
import random
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


def gettranscript(videoid):
    options = Options()
    options.add_argument("--headless")

	# Create a new instance of the Firefox driver
    if headless:
        driver = webdriver.Firefox(firefox_options=options)
    else:
        driver = webdriver.Firefox()

	# navigate to video
    driver.get("https://www.youtube.com/watch?v="+videoid)

    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "yt-icon-button.dropdown-trigger > button:nth-child(1)")))
    except:
        msg = 'could not find options button'
        driver.quit()
        return False, msg

    try:
        element.click()
    except:
        msg = 'could not click'
        driver.quit()
        return False, msg

    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#items > ytd-menu-service-item-renderer:nth-child(2) > paper-item"))) #items > ytd-menu-service-item-renderer:nth-child(2) > yt-formatted-string
    except:
        msg = 'could not find transcript in options menu'
        driver.quit()
        return False, msg

    try:
        element.click()
    except:
        msg = 'could not click'
        driver.quit()
        return False, msg

    try:
        element = WebDriverWait(driver, waittime).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-transcript-body-renderer.style-scope")))
    except:
        msg = 'could not find transcript text'
        driver.quit()
        return False, msg



    offsets = driver.find_elements_by_css_selector(".cue-group-start-offset")
    subtitles = driver.find_elements_by_css_selector(".cue.style-scope.ytd-transcript-body-renderer")
    
    jsonDict = []
    for i in range(0, len(offsets) - 1):
        sub = {
            "offset": offsets[i].text,
            "text": subtitles[i].text,
        }
        jsonDict.append(sub)

    driver.quit()

    return True, jsonDict

videoId = sys.argv[1]
tmpFileName = "tmp_" + videoId + ".json"
success, result = gettranscript(videoId)
dict = {}
if success == True:
    dict = {
        "success": success,
        "subtitles": result
    }
else: 
    dict = {
        "success": success,
        "msg": result
    }

tmpDir = "tmp/"
if not os.path.exists(tmpDir):
    os.makedirs(tmpDir)
file = open(tmpDir+ tmpFileName,"w")
file.write(json.dumps(dict))
file.close() 
print("-- Done --")