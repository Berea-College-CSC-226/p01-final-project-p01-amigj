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

import pygame
import start_screen
import end_screen
from sys import exit

from original_code.start_screen import Start_Screen




class Game:
    def __init__(self):
        """

        """
        self.wn_size = 800,600
        self.wn = pygame.display.set_mode(self.wn_size)
        self.wn.fill("white")
        self.title = pygame.display.set_caption("Scott's Cookie Conundrum")
        self.running = True
        self.clock = pygame.time.Clock()
        #maybe objects for characters like T11
            #self.scott = character-class/ig?(self.wn_size)
            #self.wizzle
            #self.wilborne
        #self.display = pygame.display.update()


        # game logic creation


    def run(self):
        """

        :return:
        """

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:



                    pygame.QUIT
                    exit()



            pygame.display.update()
            self.clock.tick(60)



        #runs the game. first opens with start screen call
        #after start screen then story construction

        #dialouge class call for box and character call.



    def if_fail(self,succeed):
        if not succeed:
            pass
            #end screen



def main():

    """
    Runs the game.
    """
    #start_screen.main()
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
