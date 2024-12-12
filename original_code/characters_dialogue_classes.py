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
#https://www.youtube.com/watch?v=G8MYGDf_9ho
####################################################################################
import pygame
import game

class Dialogue_box:
    def __init__(self):
        """
        This class creates the dialogue boxes
        :return:None
        """

    def box(self):
        """
        Creates the box
        :return: None
        """
        box = pygame.Surface((800, 175))
        box_rect = box.get_rect(midbottom = (400, 600))
        self.wn.blit(box, box_rect)

    def diag_text(self, text):
        """
        Creates the text on the first line
        :param text: Takes any custom string for dialouge for one line
        :return:None
        """
        diag_text_font = pygame.font.Font(None, 25)
        diag_text_surface = diag_text_font.render(text, True, "White")
        diag_text_surface_rect = diag_text_surface.get_rect(midbottom=(400, 460))
        self.wn.blit(diag_text_surface, diag_text_surface_rect)

    def diag_text_2(self, text):
        """
        Creates the text on the second line
        :param text: Takes any custom string for dialouge for a second line
        :return: None
        """
        diag_text_font = pygame.font.Font(None, 25)
        diag_text_surface = diag_text_font.render(text, True, "White")
        diag_text_surface_rect = diag_text_surface.get_rect(midbottom=(400, 480))
        self.wn.blit(diag_text_surface, diag_text_surface_rect)

    def diag_text_3(self, text):
        """
        Creates the text on the third line
        :param text: Takes any custom string for dialouge for a third line
        :return: None
        """
        diag_text_font = pygame.font.Font(None, 25)
        diag_text_surface = diag_text_font.render(text, True, "White")
        diag_text_surface_rect = diag_text_surface.get_rect(midbottom=(400, 500))
        self.wn.blit(diag_text_surface, diag_text_surface_rect)

class Chara:
    def __init__(self):
        """
        Creates the images of the characters
        :return: None
        """

    def neutral(self):
        """
        The neutral expression image for Scott
        :return: None
        """
        neut = pygame.image.load("neutral.png")
        neutral_scott = self.wn.blit(neut, (0,0))

    def annoyed(self):
        """
        The annoyed expression image for Scott
        :return: None
        """
        anno = pygame.image.load("annoyed.png")
        annoyed_scott = self.wn.blit(anno, (0, 0))

    def wizzle(self):
        """
        Wizzle the weasal wizard image
        :return: None
        """
        wizz = pygame.image.load("wizzletheweasalwizard.png")
        wizzle = self.wn.blit(wizz, (0, 0))

    def cookie(self):
        """
        An image of a cookie
        :return: None
        """
        cook = pygame.image.load("wizcookies.png")
        cookie = self.wn.blit(cook, (0, 0))

    def end(self):
        """
        Creepy ass lose screen image. Do not look at this screen in the dark.
        :return: None
        """
        lose = pygame.image.load("why.png")
        lose_screen = self.wn.blit(lose, (0,0))

    def win(self):
        """
        Win screen image
        :return: None
        """
        hap = pygame.image.load("happyhappyhappy.png")
        win_screen = self.wn.blit(hap, (0,0))

class Option_button:
    def __init__(self):
        """
        The buttons to make choices class
        :return: None
        """
        self.choice1_box = None
        self.choice2_box = None

    def box_draw(self):
        """
        Creates the boxes for choices 1 and 2. Choice 1 is the top box and Choice 2 is the bottom box
        :return: None
        """
        #creates the surface
        self.choice1_box = pygame.Surface((600, 40))
        self.choice2_box = pygame.Surface((600, 40))

        #creates rect for easy placement on screen
        self.choice1_box_rect = self.choice1_box.get_rect(midbottom = (400, 550))
        self.choice2_box_rect = self.choice2_box.get_rect(midbottom = (400, 600))

        #color of boxes
        self.choice1_box.fill("#56b4e8")
        self.choice2_box.fill("#efe442")

        #puts the surfaces onto the screen
        self.wn.blit(self.choice1_box, self.choice1_box_rect)
        self.wn.blit(self.choice2_box, self.choice2_box_rect)

    def choice_text(self, choice1, choice2):
        """
        Text inputs for choices 1 and 2
        :param choice1: text for choice1
        :param choice2: text for choice2
        :return: None
        """
        #for choice 1
        text_font = pygame.font.Font(None, 30)
        text_surface = text_font.render(choice1, True, "Black")
        text_surface_rect = text_surface.get_rect(midbottom=(400, 550))
        self.wn.blit(text_surface, text_surface_rect)

        #for choice 2
        text2_font = pygame.font.Font(None, 30)
        text2_surface = text2_font.render(choice2, True, "Black")
        text2_surface_rect = text2_surface.get_rect(midbottom=(400, 600))
        self.wn.blit(text2_surface, text2_surface_rect)