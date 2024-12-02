######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose: the start screen of the game
#
#######################################################################
# Acknowledgements:
# T12 teamwork
# https://docs.python.org/3/library/tkinter.html
# ChatGPT
#
#
#
####################################################################################

#import pygame, game, subprocess, tkinter as ttk
from tkinter import ttk
#from game import Game
from pygame import *
from tkinter import PhotoImage, Button

class Start_Screen:
    def __init__(self, windowtext=""):
        """
        Creates the window
        :param: Name of the window
        """
        self.root = ttk.Tk()
        self.root.minsize(width=800, height=600)
        self.root.maxsize(width=800, height=600)
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

        self.Button1 = ttk.Button(self.root, text=buttontext, command=self.button_handler1)
        self.Button1.grid(row=1,column=1)


    def create_button2(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the quit button that closes the window
        :return:
        """

        self.Button2 = ttk.Button(self.root, text=buttontext, command=self.root.destroy)
        self.Button2.grid(row=2, column=1)

    def button_handler1(self):
        """
        Event handler for the start button. This opens game.py
        :return:
        """
        #subprocess.run(["python", "game.py"]) #CBT this just reopens the start menu over and over again
        #opens the game.py file


def main():
    """
    Runs the program and creates the window
    :return:
    """

    menu = Start_Screen("Scott's Cookie Conundrum")
    menu.create_button1("Play")
    menu.create_button2("Quit")
    menu.root.mainloop()



if __name__ == "__main__":
    main()
