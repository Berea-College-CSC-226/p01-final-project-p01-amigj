######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose: the start screen of the game. Play the game by starting here and not the game file
#
#######################################################################
# Acknowledgements:
# T12 teamwork
# https://docs.python.org/3/library/tkinter.html
# ChatGPT
####################################################################################
import tkinter as tk
from tkinter import ttk
from game import *
import subprocess

class Start_Screen:
    def __init__(self, windowtext=""):
        """
        Creates the window
        :param: Name of the window
        """
        self.window = tk.Tk()
        self.window.minsize(width=800, height=600)
        self.window.maxsize(width=800, height=600)
        self.window.title(windowtext)

        #for background img
        #bkg_image = PhotoImage(file = "")

        self.Button1 = None
        self.Button2 = None


    def create_button1(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the play button that opens the game
        :return: None
        """

        self.Button1 = ttk.Button(self.window, text=buttontext, command=self.button_handler1)
        self.Button1.grid(row=1,column=1)


    def create_button2(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the quit button that closes the window
        :return: None
        """

        self.Button2 = ttk.Button(self.window, text=buttontext, command=self.window.destroy)
        self.Button2.grid(row=2, column=1)

    def button_handler1(self):
        """
        Event handler for the play button. This opens game.py
        :return: None
        """
        self.Button1 = True
        if self.Button1:
            self.window.destroy()
            subprocess.run(["python", "game.py"]) #put in a conditional for 1 click register


def main():
    """
    Runs the program and creates the window
    :return: None
    """
    menu = Start_Screen("Scott's Cookie Conundrum")
    menu.create_button1("Play")
    menu.create_button2("Quit")
    menu.window.mainloop()

if __name__ == "__main__":
    main()
