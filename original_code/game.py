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
#https://www.youtube.com/watch?v=Hujzny-gkEk
# ChatGPT
####################################################################################
import pygame
from characters_dialogue_classes import *

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

    def run(self):
        """
        The whole game loop with dialogue choices with key presses.
        :return: None
        """
        #counter for key presses
        zero_key_press_counter = 0
        one_key_press_counter = 0
        six_key_press_counter = 0

        #game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                keys = pygame.key.get_pressed()

                #keeps track of counter number
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_0]:
                        zero_key_press_counter += 1
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_1]:
                        one_key_press_counter += 1

                #easter egg/instant win button
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_6]:
                        six_key_press_counter += 1

            #default screen once the game opens
            Chara.annoyed(self)
            Dialogue_box.box(self)
            Dialogue_box.diag_text(self, "Scott: Oh no... My wizard cookies are missing!")
            Dialogue_box.diag_text_2(self,"Scott: If I don't have them, then my coding powers will be...")
            Dialogue_box.diag_text_3(self, "Scott: I need to hurry and find them!")
            Option_button.box_draw(self)
            Option_button.choice_text(self, "0) Check the fridge", "1) Summon the weasel")

            #all the different choices
            if one_key_press_counter == 0 and zero_key_press_counter == 1:
                Chara.neutral(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self,"The cookies are not in the fridge.")
                Dialogue_box.diag_text_2(self,"Only a sad peanut butter and jelly sandwich that robot Scott 2.0 tried to make.")
                Option_button.box_draw(self)
                Option_button.choice_text(self,"0) Eat the sandwich", "1) Accept your fate (Doesn't work)")

            elif one_key_press_counter == 0 and zero_key_press_counter == 2:
                Chara.end(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self, "The sandwich tasted like a failed attempt at making a sandwich.")
                Dialogue_box.diag_text_2(self,"It was fine but it wasn't wiz cookies...")
                Dialogue_box.diag_text_3(self, "You Lose and Scott never got his cookies, but a mediocre sandwich.")

            elif one_key_press_counter == 1 and zero_key_press_counter == 0:
                Chara.wizzle(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self, "You call the only wizard who knows how to fix this.")
                Dialogue_box.diag_text_2(self, "Wizzle: Wis I, Wizzle whe weasel wizard. How can I help whee?")
                Option_button.box_draw(self)
                Option_button.choice_text(self, "0) I lost the cookies", "1) Nevermind")

            elif one_key_press_counter == 2 and zero_key_press_counter == 0:
                Chara.end(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self, "Nevermind... The social anxiety was too much.")
                Dialogue_box.diag_text_2(self, "You'll be fine without the cookies. Without the powers.")
                Dialogue_box.diag_text_3(self, "You Lose. You're now a farmer helping Dan with his radish farm.")

            elif one_key_press_counter == 1 and zero_key_press_counter == 1:
                Chara.wizzle(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self,"Wizzle: You losw whe greaw wiz cookies? Ah poor scott whe wizard.")
                Dialogue_box.diag_text_2(self, "I will give you more! However, in exchange of your py swaff.")
                Option_button.box_draw(self)
                Option_button.choice_text(self, "0) Fine...", "1) Never!")

            elif one_key_press_counter == 2 and zero_key_press_counter == 1:
                Chara.end(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self,"Wizzle: Welp. You suffer when... ")
                Dialogue_box.diag_text_2(self, "You Lose. You made Wizzle upset.")

            elif one_key_press_counter == 1 and zero_key_press_counter == 2:
                Chara.win(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self, "Wizzle: Wee Hee! Here are whe precious wiz cookies!")
                Dialogue_box.diag_text_2(self, "Scott: You're the best Wiz! I'll call back next year.")
                Dialogue_box.diag_text_3(self, "You win! Hooray!")

            #instant win/easter egg
            if one_key_press_counter >= 10 or six_key_press_counter >= 3:
                Chara.win(self)
                Chara.cookie(self)
                Dialogue_box.box(self)
                Dialogue_box.diag_text(self, "You found the magic button to give Scott his cookies!")
                Dialogue_box.diag_text_2(self, "You win! By easter egg find! Now Scott won't starve!")

            #wrong key press on number pad
            if keys[pygame.K_2] or keys[pygame.K_3] or keys[pygame.K_4] or keys[pygame.K_5] or keys[pygame.K_6] or keys[pygame.K_7] or keys[pygame.K_8] or keys[pygame.K_9]:
                Chara.wrong(self)


            pygame.display.update()
            self.clock.tick(60)



def main():
    """
    Runs the game.
    :return: None
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()