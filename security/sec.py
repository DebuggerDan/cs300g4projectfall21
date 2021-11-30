# CS 300 - Group (#4) Project: ChocAn [Section: Authentication & Security, subsection: Security] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

def loginChecker(username):
    if username.isalpha() == True:
        return 1
    elif username.isnum() == True:
        if sys.getsizeof(str(username)) != 9:
            return 4
        else:
            return 3
    else:
        return 2