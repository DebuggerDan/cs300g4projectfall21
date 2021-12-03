# CS 300 - Group (#4) Project: ChocAn - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

from interface.Menus import mainMenu
from security.auth import loginGrabber, is_logged_in, is_manager


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
        print("User " + str(user[0]) + " is logged in.")  # user ID
        print("Welcome to ChocAn, " + user[1])  # username

    if is_manager(user):
        print("User is a manager.")
    else:
        print("User is not a manager.")

    mainMenu(user)

    # DB.fixService()
    # print("\nTesting service form below...\n")
    # Forms.billingForm(user)

    # Test member report function from comm.py to print member weekly report.
    # while True:
    #    testMember()

    # Test provider report function from comm.py
    # testProvider()

    # Test summary report for manager function from comm.py
    # testManager()

# NAYA TESTING
# Sam testing
