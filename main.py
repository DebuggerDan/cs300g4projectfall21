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
from security.auth import loginGrabber

#class main():

#    def __init__(self):


if __name__ == "__main__":

    print("\n\tWelcome to ChocAn!\n")

    # initiate login sequence
    logged_in = -2
    while logged_in == -2:
        logged_in = loginGrabber()
    # login successful, provider info saved in logged_in



    #print("\nTesting service form below...\n")
    #Forms.testForms()

#NAYA TESTING
#Sam testing
