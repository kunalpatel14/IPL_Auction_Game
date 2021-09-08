import pygame
import sys
import display_text
from pygame import mixer
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/select_team1.jpg')
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IPL Auction Game")
black = (0, 0, 0)
yellow = (237, 234, 52)
dark_red = (191, 34, 34)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
white = (255, 255, 255)
pink = (240, 22, 196)
mixer.music.load("music/IPL 2020 Background Music Emotional Music -- মায়াপয়েন্ট -- IPL Cricket --.mp3")
mixer.music.play()


def background_select_loop():
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_display.blit(background_page_1, (0, 0))
        display_text.display_text(game_display,"Select Your Team For the Auction", light_blue, 'arial', 690, 68, 80)
        csk = tranparent_button_select(game_display, "hi", 150, 226, 240, 200, red, light_blue, 'csk')
        mi = tranparent_button_select(game_display, "hi", 470, 226, 240, 200, red, light_blue, 'mi')
        rcb = tranparent_button_select(game_display, "hi", 790, 226, 240, 200, red, light_blue, 'rcb')
        kkr = tranparent_button_select(game_display, "hi", 1110, 226, 240, 200, red, light_blue, 'kkr')
        srh = tranparent_button_select(game_display, "hi", 150, 499, 240, 200, red, light_blue, 'srh')
        dc = tranparent_button_select(game_display, "hi", 470, 499, 240, 200, red, light_blue, 'dc')
        pk = tranparent_button_select(game_display, "hi", 790, 499, 240, 200, red, light_blue, 'pk')
        rr = tranparent_button_select(game_display, "hi", 1110, 499, 240, 200, red, light_blue, 'rr')
        if csk == 1:
            print('csk')
            return 'csk'
        elif mi == 2:
            print('mi')
            return 'mi'
        elif rcb == 3:
            print('rcb')
            return 'rcb'
        elif kkr == 4:
            print('kkr')
            return 'kkr'
        elif srh == 5:
            print('srh')
            return 'srh'
        elif dc == 6:
            print('dc')
            return 'dc'
        elif pk == 7:
            print('pk')
            return 'pk'
        elif rr == 8:
            print('rr')
            return 'rr'
        pygame.display.update()


def tranparent_button_select(game_display, msg, x, y, w, h, ic, ac, action=None,):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        if (click[0] == 1) and (action != None):
            if action == 'csk':
                return 1
            elif action == 'mi':
                return 2
            elif action == 'rcb':
                return 3
            elif action == 'kkr':
                return 4
            elif action == 'srh':
                return 5
            elif action == 'dc':
                return 6
            elif action == 'pk':
                return 7
            elif action == 'rr':
                return 8
    else:
        return -1
