'''
################################################################
### Simple Python to read and click on the + Linkedin button ###
### Please refactor and use classes properly, thx!           ###
### Copyright libremente - GPLv3 - Feel free!                ###
################################################################
'''
from tkinter import Tk, X, LEFT, IntVar
from tkinter import Frame, Label, Entry, Button, Checkbutton, messagebox
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 

import time


def launch_driver(user, pwd, checkedValue):
    ''' Open webdriver '''
    driver = webdriver.Firefox()
    driver.get("https://www.linkedin.com/?trk=nav_header_logo")

    # Login
    username = driver.find_element_by_id('login-email')
    username.send_keys(user)
    password = driver.find_element_by_id('login-password')
    password.send_keys(pwd)
    driver.find_element_by_id('login-submit').click()

    # If we want to add everyone to the friends list, then call the function
    if checkedValue == 1:
        click_friends(driver)
    # Eventually, call the function for pushing the button
    click_plus(driver)

    # Print message and bye
    messagebox.showinfo("Well Done!", "From surF with love ;)")


def click_plus(driver):
    ''' Push the plus button '''
    # Read file
    with open('out.txt') as fin:
        for line in fin:
            # Get line and browse it
            driver.get(line)
            time.sleep(5)
            try:
                elements = driver.find_elements_by_class_name('button-secondary-medium-round')
                # Eventually push the button!
                for el in elements:
                    el.click()
            except NoSuchElementException:
                pass
                # Everywhere you go, everything you say, in TPI you gotta scream my name! Thesurfa!


def click_friends(driver):
    ''' Add a friend request '''
    # Read file
    with open('out.txt') as fin:
        for line in fin:
            # Get line and browse it
            driver.get(line)
            time.sleep(5)
            try:
                # First click on "Collegati"
                connect = driver.find_element_by_class_name('pv-s-profile-actions--connect')
                connect.click()
                time.sleep(2)
                # Then click on "ok"
                alert = driver.find_element_by_css_selector('.send-invite__actions > .button-primary-large')
                alert.click()
                time.sleep(1)
            except Exception as e:
                print(e)
                pass


# Retrieve input fun
def retrieve_input(checkedValue):
    ''' Retrieve the values inserted by the tkInter interface '''
    user = usernameEntry.get()
    pwd = pwdEntry.get()

    if not user or not pwd:
        messagebox.showinfo("Errore", "User or Pwd not correctly inserted")

    launch_driver(user, pwd, checkedValue)


''' Main script'''
''' Now global, please refactor and use Classes! '''
# Setup the tkinter interface
top = Tk()
top.title("I click for you!")

label = Label(text="LinkedIn Clicker")
label.pack()

frame1 = Frame()
frame1.pack(fill=X)

usernameLabel = Label(frame1, text="User", width=20)
usernameLabel.pack(side=LEFT, padx=5, pady=5)

usernameEntry = Entry(frame1)
usernameEntry.pack(fill=X, padx=5, expand=True)

frame2 = Frame()
frame2.pack(fill=X)

pwdLabel = Label(frame2, text="Password", width=20)
pwdLabel.pack(side=LEFT, padx=5, pady=5)

pwdEntry = Entry(frame2, show="*")
pwdEntry.pack(fill=X, padx=5, expand=True)

checkValue = IntVar()
checkButton = Checkbutton(top, text="Tutti Amici!", onvalue=1, offvalue=0, variable=checkValue)
checkButton.pack()

submitButton = Button(text="Run Fast!", command=lambda: retrieve_input(checkValue.get()))
submitButton.pack()

# Main loop
top.mainloop()
