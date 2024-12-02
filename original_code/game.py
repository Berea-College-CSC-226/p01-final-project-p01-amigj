######################################################################
# Author: Janee Amig
# Username: Amigj
#
# P01: Final Project
#
# Purpose: the game itself. A chose your own adventure of you being Scott the wizard
# looking for his long lost wizard cookies.
#######################################################################
# Acknowledgements:
# T011
# T04
# T01
#
#
#
#

####################################################################################

import pygame, start_screen, end_screen

from original_code.start_screen import Start_Screen




class Game:
    def __init__(self):
        """

        """
        #creates the window
        # game clock/tick
        # game logic creation


    def run(self):
        """

        :return:
        """

        #runs the game. first opens with start screen call
        #after start screen then story construction

        #dialouge class call for box and character call.


        #story
            #late at night and wake up for cookies, but oh no its gone

            #option to look around: the fridge, pocket, shadow realm etc...
                #pocket: the pocket has lint and bugs in it but no cookies.
                #fridge: a note reading sorry I ate your cookies
                #darkweb: the basement did not have your cookies. Besides I think its a bit too dangerous looking in there for them

            #you ask/blame roomie but roomie is clueless
            #You found cookies! but its internet cookies...Ah great...Lose
            #you find the wizzle the weasel wizard and ask for more cookies
            #the wizzle is dissappointed but gives you it's cookies. Fun fact the chips are not chocolate. Win


def main():

    """

    """
    start_game = start_screen.main()

    #game = Game()
    #game.run()


if __name__ == "__main__":
    main()
