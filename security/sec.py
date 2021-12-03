# CS 300 - Group (#4) Project: ChocAn [Section: Authentication & Security, subsection: Security] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang
import sys


def loginChecker(username):
    if username.isalpha():
        return 1  # deprecated. was supposed give option to use name instead of ID, but was tossed
    elif username.isnumeric():
        # this is the memory size of the object not the number of characters
        # if sys.getsizeof(str(username)) != 9:
        if len(username) != 9:
            return 4  # number, but isnt right size
        else:
            return 3  # correct
    else:
        return 2  # not numerical / alphabetical


def serviceChecker(service):
    if not service.isnumeric():
        return 1  # isn't a number
    # elif sys.getsizeof(str(service)) != 6:
    elif len(service) != 6:
        return 2  # number is wrong size
    else:
        return 3  # correct


def nameChecker(name):
    if name.isnumeric():
        return 1  # is a number
    elif name.isalnum():
        return 2  # is alphanumeric
    elif any(x.isalpha() for x in name) and any(x.isspace() for x in name) and all(
            x.isalpha() or x.isspace() for x in name):
        return 3  # contains at least one letter and one space (correct)
    else:
        return 4  # not a number, alphanumeric, or a string with one letter and one space


# extra function to validate number in range
def rangeChecker(num, minimum, maximum):  # changed min/max to minimum/maximum as min/max shadow built-in functions
    if not num.isnumeric():
        return 1  # isn't a number
    elif int(num) < minimum:
        return 2  # too small
    elif int(num) <= maximum:
        return 3  # correct
    else:
        return 4  # too big


def isPhonenum(numb):
    filterseq = [' ', '(', ')', '-']  # list of items to filter
    Tphonenum = filter(filterseq, numb)  # populates a temp phonenum var with a filtered number
    # note: this is needed because of the different types of phone number formats used
    if Tphonenum.isnumeric() == True and sys.getsizeof(str(Tphonenum)) == 10:
        return 3  # if it's a number and 10 digits long (correct)
    elif Tphonenum.isalnum():
        return 1  # other letters present in phone number somehow
    else:
        return 2  # other extraneous characters present


def isValidSelection(choice):
    choiceAmt = 7  # change to be the proper number of choices
    if not choice.isnumeric():
        return 1
    elif sys.getsizeof(choice) > choiceAmt:
        return 2
    else:
        return 3
