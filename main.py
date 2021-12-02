# CS 300 - Group (#4) Project: ChocAn - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

import numpy as np
import os
import sys
import json
import logging
import functools
from datetime import datetime, timedelta
from playsound import playsound
from interface.forms import Forms
from security.auth import loginGrabber, is_logged_in, is_manager
from database.database import Database as DB

#class main():

#    def __init__(self):


if __name__ == "__main__":

    print("\tWelcome to ChocAn!\n")

    # for assistance logging in try the following ids
    # 100000001 (manager)
    # 200000001 (provider)

    # initiate login sequence
    user = -2
    while user == -2:
        user = loginGrabber()
    # login successful, provider info saved in logged_in

    if is_logged_in(user):
        print("User " + str(user[0]) + " is logged in.") #user ID
        print("Welcome to ChocAn, " + user[1]) #user name

    if is_manager(user):
        print("User is a manager.")
    else:
        print("User is not a manager.")


    print("\nTesting service form below...\n")
    #Forms.billingForm(user)


#NAYA TESTING
#Sam testing
