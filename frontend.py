# Please only use this program in good faith.
# Software under the 0BSD license, aka do whatever you'd like with it!

from operator import itemgetter
from selenium.webdriver.support.ui import Select
# Import platform to receive system info from user
import platform
# Import Selenium -> webdriver
from selenium import webdriver

def main():
    # Check if user is using MacOS or Windows
    def finduseros():
        global useros
        useros = platform.system()
        if "Darwin" in useros:
            useros= "macos"
        if "Windows" in useros:
            useros="windows"
        print("Current user's OS is: " + useros)
        return useros

    def logininfo():
        global username, password
        # Query user for universal login info
        username = input(str("What is your Universal username?"))
        password = input(str("What is your password?"))
        print("Username: ", username)
        print("Password: ", password)
        return username, password

    def crn():
        global crn1, crn2, crn3
        # Query user for CRN
        crn = input(str("What are the CRNs for your classes? (Seperate by comma!)"))
        crnlist = list(crn.split(','))
        crn1 = crnlist[0]
        crn2 = crnlist[1]
        crn3 = crnlist[2]
        return crn1, crn2, crn3

    # Run finduseros
    finduseros()

    # Run logininfo
    logininfo()

    # Run crn
    crn()

    def runbot():
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
