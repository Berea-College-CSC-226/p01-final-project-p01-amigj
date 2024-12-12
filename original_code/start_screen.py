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
# https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
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
        :return: None
        """
        self.window = tk.Tk()
        self.window.minsize(width=220, height=300)
        self.window.maxsize(width=220, height=300)
        self.window.title(windowtext)
        self.button1 = None
        self.button2 = None
        self.textlabel1text = tk.StringVar()
        self.textlabel1 = None

    def create_button1(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the play button that opens the game
        :return: None
        """
        self.button1 = tk.Button(self.window, text=buttontext, command=self.button_handler1)
        self.button1.grid(row=9, column=1, ipadx=40)

    def create_button2(self, buttontext="push"):
        """
        Creates the button
        :param buttontext: the quit button that closes the window
        :return: None
        """
        self.button2 = tk.Button(self.window, text=buttontext, command=self.window.destroy)
        self.button2.grid(row=10, column=1, ipadx=40)

    def create_label1(self, labeltext=""):
        """
        Creates the label text
        :param labeltext: an empty string that will be filled in the main function
        :return: None
        """
        self.textlabel1text.set(labeltext)
        self.textlabel1 = tk.Label(self.window, textvariable=self.textlabel1text)
        self.textlabel1.grid(row = 1, column = 1)

    def button_handler1(self):
        """
        Event handler for the play button. This opens game.py
        :return: None
        """
        self.button1 = True
        if self.button1:
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
    menu.create_label1("Scott's Cookie Conundrum \n"
                       "It's your job to help him find \n"
                       "his long lost wizard cookies\n"
                       "before it's too late!\n"
                       "\n"
                       "How to play:\n"
                       "Press '0' or '1'\n"
                       "on your keyboard to progress the story.\n"
                       "If you get end screen,\n"
                       "just exit and run the program\n"
                       "to try again.\n")
    menu.window.mainloop()

if __name__ == "__main__":
    main()
