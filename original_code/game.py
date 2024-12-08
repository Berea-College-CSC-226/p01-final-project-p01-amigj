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
# https://stackoverflow.com/questions/54191913/pygame-window-opens-and-instantly-closes
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
        self.wn_size = 800,600
        self.wn = pygame.display.set_mode(self.wn_size)
        self.running = True
        self.wn.fill("white")
        self.time = pygame.time.Clock()
        #maybe objects for characters like T11
            #self.scott = character-class/ig?(self.wn_size)
            #self.wizzle
            #self.wilborne


        # game logic creation


    def run(self):
        """

        :return:
        """

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


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





        pygame.QUIT



def main():

    """

    """
    # start_game = start_screen.main()
    Game()
    #game = Game()
    #game.__init__()


if __name__ == "__main__":
    main()
