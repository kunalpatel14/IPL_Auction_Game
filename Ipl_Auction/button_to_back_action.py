import pygame
import sys
import background_page_1
import background_page_1


def back_tranparent_button(game_display, msg, x, y, w, h, ic, ac, action=None):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        if (click[0] == 1) and (action != None):
            if action == 'quit_icon':
                pygame.quit()
                quit()
                sys.exit()
            elif action == 'back_to_menu_icon':
                background_page_1.background_1_loop()
                return

