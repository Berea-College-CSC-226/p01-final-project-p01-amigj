######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose: Classes of dialogue, character model, and choice buttons
#
#######################################################################
# Acknowledgements:
#https://www.youtube.com/watch?v=Y_ghJY-sW3o
#https://www.pygame.org/docs/ref/rect.html
#https://stackoverflow.com/questions/54191913/pygame-window-opens-and-instantly-closes
#
#
#
#
#
#
####################################################################################
from tkinter. font import names


class Dialogue:
    def __init__(self, name, text):
        """
        creates the box
        """

        self.name = name #name of character
        self.text = text #should be a string

    def rect(self):
        """

        :return:
        """

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
        """

        :param choice:
        """
        self.choice = choice

        #creates the button
        #choice is a string that can have text input
        #register click
