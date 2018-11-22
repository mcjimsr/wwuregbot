# Please only use this program in good faith.
# Software under the 0BSD license, aka do whatever you'd like with it!

from operator import itemgetter
from selenium.webdriver.support.ui import Select
# Import platform to receive system info from user
import platform
# Check if user is using MacOS or Windows
def finduseros():
    useros = platform.system()
    if "Darwin" in useros:
        useros= "macos"
    if "Windows" in useros:
        useros="windows"
    print("Current user's OS is: " + useros)

# Query user for universal login info
username = input(str("What is your Universal username?"))
password = input(str("What is your password?"))

# Query user for CRN
crn = input(str("What are the CRNs for your classes? (Seperate by comma!)"))
crnlist = list(crn.split(','))
crn1 = crnlist[0]
crn2 = crnlist[1]
crn3 = crnlist[2]

# Run finduseros
finduseros()

# Import Selenium -> webdriver
from selenium import webdriver

# Set browser to Chrome
browser = webdriver.Chrome('/Users/rmcj/PycharmProjects/WWU Registration Bot/chromedriver')

# Go to registration page
browser.get('https://admin.wwu.edu/pls/wwis/bwskfreg.P_AltPin')

# Find username entry box
usernameentry = browser.find_element_by_xpath("""//*[@id="username"]""")
# Send username to username entry box
usernameentry.send_keys(username)
# Find password entry box
passwordentry = browser.find_element_by_xpath("""//*[@id="password"]""")
# Send password to password entry box
passwordentry.send_keys(password)


# Find "login" button, save to var
loginbutton = browser.find_element_by_xpath("""//*[@id="fm1"]/section[4]/input[4]""")
# Click "login" button
loginbutton.click()

# Find Term drop down menu
termselect = Select(browser.find_element_by_xpath("""//*[@id="term_id"]"""))
# If registration time not ready, refresh webpage
if termselect is not browser:
    browser.refresh()

submitbutton = browser.find_element_by_xpath("""/html/body/div[3]/form/input""")
submitbutton.click()

# Insert CRNs for user
crnentry1 = browser.find_element_by_xpath("""//*[@id="crn_id1"]""")
crnentry1.send_keys(crn1)

crnentry2 = browser.find_element_by_xpath("""//*[@id="crn_id2"]""")
crnentry2.send_keys(crn2)

crnentry3 = browser.find_element_by_xpath("""//*[@id="crn_id3"]""")
crnentry3.send_keys(crn3)

# Click submit button
submitcrns = browser.find_element_by_xpath("""/html/body/div[3]/form/input[19]""")
submitcrns.click()

# Class add errors
#errordetect = browser.find_element_by_xpath("""/html/body/div[3]/form/table[3]/tbody/tr/td[2]/span""")


