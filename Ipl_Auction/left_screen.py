import pygame
import sys
import display_text
import pygane_button
import right_screen
import team_class
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/1_auction_hall_with_temp1.jpg')
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


def background_left_loop():
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_display.blit(background_page_1, (0, 0))
        font1 = pygame.font.SysFont('arialblack', 18)
        img1 = font1.render("Virat kohli", True, black)
        font2 = pygame.font.SysFont('arialblack', 20)
        img2 = font2.render("200 L", True, black)
        game_display.blit(img1, (30, 240))
        game_display.blit(img2, (170, 240))

        font3 = pygame.font.SysFont('arialblack', 15)
        img3 = font3.render("Current", True, black)
        game_display.blit(img3, (35, 285))
        font4 = pygame.font.SysFont('arialblack', 15)
        img4 = font4.render("Bid", True, black)
        game_display.blit(img4, (35, 305))
        font4 = pygame.font.SysFont('arialblack', 30)
        img4 = font4.render("₹1500", True, black)
        game_display.blit(img4, (120, 285))

        font5 = pygame.font.SysFont('arialblack', 20)
        img5 = font5.render("By :", True, black)
        game_display.blit(img5, (35, 360))

        font6 = pygame.font.SysFont('arialblack', 30)
        img6 = font6.render("CSK", True, black)
        game_display.blit(img6, (100, 350))

        pygame.display.update()


background_left_loop()
quit()
sys.exit()