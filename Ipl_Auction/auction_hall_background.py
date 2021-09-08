import pygame
import sys
import display_text
import pygane_button
import right_screen
import team_class
from pygame import mixer
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/1_auction_hall.jpg')
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
team_detail = []
team_detail.append(team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
mixer.music.load("music/welcome.mp3")
mixer.music.play()
mixer.music.load("music/IPL 2020 Background Music Emotional Music -- মায়াপয়েন্ট -- IPL Cricket --.mp3")
mixer.music.set_volume(1)
mixer.music.play()

first_time = 0
i = 0


def background_1_loop():
    global i
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_display.blit(background_page_1, (0, 0))
        display_text.display_text(game_display, "Welcome", light_blue,'algerian', 748.5, 280, 50)
        display_text.display_text(game_display, "To", light_blue, 'algerian', 748.5, 330, 20)
        display_text.display_text(game_display, "IPL Auction Game", light_blue, 'algerian', 748.5, 380, 50)
        display_text.display_text(game_display, "Click on Above Button To Start Game", red, 'algerian', 748.5, 480, 20)
        pygane_button.button(game_display, "Start Game", 698.5, 420, 120, 30, dark_red, red, 'start_game')
        pygane_button.tranparent_button(game_display, "hii", 1258, 230, 240, 195, red, light_blue, 'summary')
        pygane_button.tranparent_button(game_display, "hii", 36, 20, 50, 50, red, light_blue, team_detail, 'instruction_icon')
        pygane_button.tranparent_button(game_display, "hii", 1430, 1, 80, 70, red, light_blue, team_detail, 'quit_icon')
        pygane_button.tranparent_button(game_display, "hii", 1350, 1, 70, 70, red, light_blue, team_detail, 'back_to_menu_icon')
        right_screen.right_screen(game_display, team_detail)
        pygane_button.tranparent_button(game_display, "hii", 1080, 650, 180, 90, red, light_blue, 'team_players')
        pygame.display.update()





