# CS 300 - Group (#4) Project: ChocAn [Section: Authentication & Security] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang


# planning for functions n stuff here.
from database.database import Database
from interface.forms import Forms


def loginGrabber():
    # take user input for login.
    # username = input('Enter a username: ')
    # check to make sure it's ok
    # charCheck = loginChecker(username)
    # if charCheck != 3:
    #    print("Error: Improper login input!")
    #    return -1
    # passes sanitized entries to database control function

    # switching over to the provider ID input form
    # which uses auth.py to validate the provider ID
    username = 0
    while username == 0:
        username = Forms.providerIDForm()

    loginSuccess = loginDatabaseControl(username, 3)
    # if loginSuccess != None:
    if str(loginSuccess) != "None":
        print("Login success... Sending data...\n")

        return loginSuccess
    else:
        print("ID not found. Please try again!")
        return -2


# expand below function to run through checking what type (provider / patient / etc) the ID matches
def loginDatabaseControl(username, charCheck):
    if charCheck == 3:
        # userData = get_provider(username)
        userData = Database.get_provider(username)

        return userData


def is_logged_in(user):
    if user == -2:
        return False
    return True


def is_manager(user):
    if not is_logged_in(user):
        return False
    tempID = str(user[0])
    if tempID[0] == "1":
        return True
    else:
        return False

