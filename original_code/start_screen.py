######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose:
#
from tkinter import PhotoImage

#######################################################################
# Acknowledgements:
# T12 teamwork
#
#
####################################################################################

import pygame, tkinter as tk


class Start_Screen:
    def __init__(self, windowtext=""):
        """
        Creates the window
        :param: Name of the window
        """
        self.root = tk.Tk()
        self.root.minsize(width=600, height=800)
        self.root.maxsize(width=600, height=800)
        self.root.title(windowtext)

        #for background img
        #bkg_image = PhotoImage(file = "")

        self.Button1 = None
        self.Button2 = None


    def create_button1(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the start button that opens the game
        :return:
        """

        self.Button1 = tk.Button(self.root, text=buttontext, command=self.button_handler1)
        self.Button1.pack


    def create_button2(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the quit button that closes the window
        :return:
        """
        self.Button2 = tk.Button(self.root, text=buttontext, command=self.button_handler2)
        self.Button2.pack

    def button_handler1(self):
        """
        Event handler for the start button. This opens game.py
        :return:
        """

        #opens the game.py file

    def button_handler2(self):
        """
        Event handler for the quit button. This closes the window
        :return:
        """

        #exits the window


def main():
    """
    Runs the program and creates the window
    :return:
    """

    menu = Start_Screen("Scott's Cookie Conundrum")
    menu.Button1("Play")
    menu.Button2("Quit")
    menu.root.mainloop()

    pass

if __name__ == "__main__":
    main()
