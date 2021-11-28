# CS 300 - Group (#4) Project: ChocAn [Section: Authentication & Security] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang



# planning for functions n stuff here.
from pkg_resources import get_provider
from security.sec import loginChecker


def loginGrabber():
    #take user input for login.
    username = input('Enter a username: ')
    #check to make sure it's ok
    charCheck = loginChecker(username)
    if charCheck == 3:
        print("Error: Improper login input!")
        return -1
    #passes sanitized entries to database control function
    loginSuccess = loginDatabaseControl(username, charCheck)
    if loginSuccess != None:
        print("Login success... Sending data...\n")
        return loginSuccess
    else:
        print("ID not found. Please try again!")
        return -2

    #expand below function to run through checking what type (provider / patient / etc) the ID matches
def loginDatabaseControl(username, charCheck):
    #does some database stuff, calling get provider / get provider by name depending on charCheck's value
    ##if charCheck == 1:
    ##    userData = get_provider_by_name(username)
    ##    return userData
    if charCheck == 2:
        userData = get_provider(username)
        return userData
