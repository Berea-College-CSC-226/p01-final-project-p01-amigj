######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose: End Screen to report win or loss
#

#######################################################################
# Acknowledgements:
# T11 code
# https://www.pygame.org/docs/ref/display.html
#
####################################################################################

import pygame, game
class End_screen:

    def __init__(self):
        """
        Creates the end screen.
        :return:
        """
        wn = pygame.display.set_mode((800,600))
        #placeholder text
        #optional:bkg image

        #close wn on click or a button for quit


class End_screen_win(End_screen):
    def __init__(self):
        super().__init__()
        #optional:shows the image of the end screen if win
        # replace text with win text

class End_screen_lose(End_screen):
    def __init__(self):
        super().__init__()
        #optional:shows the image pf the end screen if lose
        # replace txt with lose txt

End_screen()