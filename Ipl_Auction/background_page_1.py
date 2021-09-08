import pygame
import pygane_button
import sys
from pygame import mixer
import text_to_speech
import time
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/ipl_auction_background_1.jpg')
background_page_2 = pygame.image.load('photo/backgound_with_text.jpg')
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IPL Auction Game")
clock = pygame.time.Clock()
black = (5, 5, 5)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
mixer.init()
mixer.music.load('music/IPL Theme (feat. Dj Monster PS)_160k.mp3')
mixer.music.play()
mixer.music.set_volume(0.5)


def text_objects(text, font):
    textsurf = font.render(text, True, black)
    return textsurf, textsurf.get_rect()


def message_display(text, x, y):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = (x, y)
    game_display.blit(textsurf, textrect)
    return


def background_1_loop():
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_display.blit(background_page_2, (0, 0))
        pygane_button.button(game_display, 'Start Game', 100, 700, 150, 50, light_blue, light_b, 'start_new_game')
        pygane_button.button(game_display, 'Resume Game', 300, 700, 150, 50, light_blue, light_b, 'resume_game')
        pygane_button.button(game_display, 'Instructions', 500, 700, 150, 50, light_blue, light_b, 'quit')
        pygane_button.button(game_display, 'Quit', 1300, 700, 150, 50, light_blue, light_b, 'quit')
        pygame.display.update()


background_1_loop()
quit()
sys.exit()
