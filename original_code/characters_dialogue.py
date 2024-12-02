######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose:
#
#######################################################################
# Acknowledgements:
#
#
#
####################################################################################
from tkinter.font import names


class Dialogue:
    def __init__(self, name, text):
        """
        creates the box
        """

        self.name = name #name of character
        self.text = text #should be a string

        #create two boxes. One large one for text one small one for name
        #the boxes are in a fixed position (bottom center)
        #bkg color will always be white
        #register on click



class Characters:
    def __init__(self):
        """
        creates the characters
        """

        #box for charcater as placeholder
        # (the parameter should take character img/convert img into a easy variable like:
        # neutral_scott = unititled14.png
        # happy_scott = untitled23.png etc.....)

        #blue box for scott
        #orange box for wiz
        #purple box for wilborne (do ask her)

class Option:
    def __init__(self, choice):
        self.choice = choice

        #creates the button
        #choice is a string that can have text input
        #register click
