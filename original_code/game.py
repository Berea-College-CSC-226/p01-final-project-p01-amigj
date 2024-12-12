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
# https://www.pygame.org/docs/ref/key.html
#
#

####################################################################################

import pygame
import start_screen
import end_screen
from sys import exit
from characters_dialogue_classes import *
from original_code.characters_dialogue_classes import Option_button


class Game:
    def __init__(self):
        """
        Creation of game logic (screen, time, title, etc.)
        :return: None
        """
        pygame.init()
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

    def box_text(self, text):

        text_font = pygame.font.Font(None, 50)
        text_surface = text_font.render(text, True, "Red")
        text_surface_rect = text_surface.get_rect(midbottom=(400, 450))
        self.wn.blit(text_surface, text_surface_rect)
        #delete later this is a test/back up if things go wrong

    def run(self):
        """

        :return:
        """
        #game loop
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #self.box_text("hello")
            #register keyboad presses for options
            pygame.k

            Chara.annoyed(self)
            Dialogue_box.box(self)
            Dialogue_box.diag_text(self, "Great scott Marty")
            Option_button.box_draw(self)
            Option_button.choice_text(self, "hello", "bye")



            pygame.display.update()
            self.clock.tick(60)



        #runs the game. first opens with start screen call
        #after start screen then story construction

        #dialouge class call for box and character call.



    def if_fail(self,succeed):
        '''

        :param succeed:
        :return:
        '''
        if not succeed:
            pass
#end screen



def main():
    """
    Runs the game.
    :return: None
    """
    #start_screen.main()
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
