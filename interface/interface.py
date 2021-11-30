# CS 300 - Group (#4) Project: ChocAn [Section: Database, subsection: Logging] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang

import tkinter as gui

def main_screen():
    global main_screen
    main_screen = gui.Tk()

    main_screen.geometry("420x69")
    main_screen.title("ChocAn - Provider Login")

    gui.Button(main_screen, text="Login", command=login).pack()

def login():
    global lscreen, username, password, usertemp, passtemp
    username = gui.StringVar()
    password = gui.StringVar()
    lscreen = gui.Toplevel(main_screen)

    lscreen.title("Chocoholics Anonymous - Provider Login")
    lscreen.geometry("420x69")

    gui.Label(lscreen, text="Welcome! Please enter your ChocAn Provider Credentials!").pack()

    gui.Label(lscreen, text="ChocAnUsername:").pack()
    gui.Entry(lscreen, textvariable=username).pack()

    gui.Label(lscreen, text="ChocAn Password:").pack()
    gui.Entry(lscreen, textvariable=password, show="*").pack()

    gui.Button(lscreen, text="Login", command=userauth).pack()

def userauth():
    global lscreen, usertemp, passtemp
    usertemp = username.get()
    passtemp = password.get()
    lscreen.destroy()
