# Please only use this program in good faith.
# Software under the 0BSD license, aka do whatever you'd like with it!

from selenium.webdriver.support.ui import Select
# Import platform to receive system info from user
import platform
# Import Selenium -> webdriver
from selenium import webdriver
# Import PySimpleGUI
import PySimpleGUI as SG
# Import os
import os

def main():
    # Check if user is using MacOS or Windows
    def finduseros():
        global useros
        global cd
        filename = "frontend.py"
        useros = platform.system()
        if "Darwin" in useros:
            useros= "macos"
            cd = "chromedriverMac"
        if "Windows" in useros:
            useros="windows"
            cd = "chromedriverWindows"

        userpath = os.getcwd()
        cd = str(userpath) + "/" + cd
        #print(userpath)
        #print(cd)

        return useros

    def logininfo():
        global username, password
        username = SG.PopupGetText('Please type your username:', 'Username')
        password = SG.PopupGetText('Please type your password:', 'Password', password_char='*')
        return username, password

    def crn():
        global crn1, crn2, crn3, crn4, crn5
        # Query user for CRN
        crn1 = SG.PopupGetText('Please type your first desired CRN:', 'CRN 1')

        while len(crn1) is not 5:
            SG.Popup('This CRN is not valid. Please try again.')
            crn1 = SG.PopupGetText('Please type your first desired CRN:', 'CRN 1')

        crn2 = SG.PopupGetText('Please type your second desired CRN:', 'CRN 2')
        while len(crn2) is not 5:
            SG.Popup('This CRN is not valid. Please try again.')
            crn2 = SG.PopupGetText('Please type your second desired CRN:', 'CRN 2')

        crn3 = SG.PopupGetText('Please type your third desired CRN:', 'CRN 3')
        while len(crn3) is not 5:
            SG.Popup('This CRN is not valid. Please try again.')
            crn3 = SG.PopupGetText('Please type your third desired CRN:', 'CRN 3')

        crn4 = SG.PopupGetText('Please type your fourth desired CRN: (If unneccesary, type "none")', 'CRN4')
        if (len(crn4) is not 5) and crn4 != "none":
            SG.Popup('This CRN is not valid. Please try again.')
            crn5 = SG.PopupGetText('Please type your fourth desired CRN: (If unneccesary, type "none")', 'CRN4')

        crn5 = SG.PopupGetText('Please type your fifth desired CRN: (If unneccesary, type "none")', 'CRN5')
        if (len(crn5) is not 5) and crn5 != "none":
            SG.Popup('This CRN is not valid. Please try again.')
            crn5 = SG.PopupGetText('Please type your fifth desired CRN: (If unneccesary, type "none")', 'CRN5')

        # Print CRNs
        print(crn1, crn2, crn3)
        if crn4 is not "none":
            print("CRN 4 not active.")
        if crn5 is not "none":
            print("CRN 5 not active.")



    # Run finduseros
    finduseros()

    # Run logininfo
    logininfo()

    # Run crn
    crn()

    def runbot():
        # Set browser to Chrome
        browser = webdriver.Chrome(cd)

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

    # Run runbot
    runbot()

# Run main
main()

