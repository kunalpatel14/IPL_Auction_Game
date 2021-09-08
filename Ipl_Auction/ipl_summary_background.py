import pygame
import sys
import display_text
from pygame import mixer
import pygane_button
import team_class
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/ipl_summary.jpg')
summary_game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IPL Auction Game")
black = (0, 0, 0)
yellow = (237, 234, 52)
dark_red = (191, 34, 34)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
white = (255, 255, 255)
pink = (240, 22, 196)


def title(team_detail):
    display_text.display_text(summary_game_display, "Teams", yellow, 'bahnschrift', 480, 80, 100)
    display_text.display_text(summary_game_display, "Money", yellow, 'bahnschrift', 820, 40, 40)
    display_text.display_text(summary_game_display, "( CR )", yellow, 'bahnschrift', 820, 100, 40)
    display_text.display_text(summary_game_display, "Players", yellow, 'bahnschrift', 1030, 100, 40)
    display_text.display_text(summary_game_display, "Total", yellow, 'bahnschrift', 1000, 40, 40)
    display_text.display_text(summary_game_display, "Players", yellow, 'bahnschrift', 1190, 100, 40)
    display_text.display_text(summary_game_display, "Foreign", yellow, 'bahnschrift', 1190, 40, 40)

    display_text.display_text(summary_game_display, "CSK", white, 'bahnschrift', 420, 190, 70)
    display_text.display_text(summary_game_display, str(team_detail[0].remaining_money), white, 'bahnschrift', 840, 190, 70)
    display_text.display_text(summary_game_display, str(team_detail[0].total_players), white, 'bahnschrift', 1030, 190, 70)
    display_text.display_text(summary_game_display, str(team_detail[0].foreign), white, 'bahnschrift', 1190, 190, 70)

    display_text.display_text(summary_game_display, "MI", white, 'bahnschrift', 420, 270, 70)
    display_text.display_text(summary_game_display, str(team_detail[1].remaining_money), white, 'bahnschrift', 840, 270, 70)
    display_text.display_text(summary_game_display, str(team_detail[1].total_players), white, 'bahnschrift', 1030, 270, 70)
    display_text.display_text(summary_game_display, str(team_detail[1].foreign), white, 'bahnschrift', 1190, 270, 70)

    display_text.display_text(summary_game_display, "RCB", white, 'bahnschrift', 420, 350, 70)
    display_text.display_text(summary_game_display, str(team_detail[2].remaining_money), white, 'bahnschrift', 840, 350, 70)
    display_text.display_text(summary_game_display, str(team_detail[2].total_players), white, 'bahnschrift', 1030, 350, 70)
    display_text.display_text(summary_game_display, str(team_detail[2].foreign), white, 'bahnschrift', 1190, 350, 70)

    display_text.display_text(summary_game_display, "KKR", white, 'bahnschrift', 420, 430, 70)
    display_text.display_text(summary_game_display, str(team_detail[3].remaining_money), white, 'bahnschrift', 840, 430, 70)
    display_text.display_text(summary_game_display, str(team_detail[3].total_players), white, 'bahnschrift', 1030, 430, 70)
    display_text.display_text(summary_game_display, str(team_detail[3].foreign), white, 'bahnschrift', 1190, 430, 70)

    display_text.display_text(summary_game_display, "SRH", white, 'bahnschrift', 420, 510, 70)
    display_text.display_text(summary_game_display, str(team_detail[4].remaining_money), white, 'bahnschrift', 840, 510, 70)
    display_text.display_text(summary_game_display, str(team_detail[4].total_players), white, 'bahnschrift', 1030, 510, 70)
    display_text.display_text(summary_game_display, str(team_detail[4].foreign), white, 'bahnschrift', 1190, 510, 70)

    display_text.display_text(summary_game_display, "DC", white, 'bahnschrift', 420, 580, 70)
    display_text.display_text(summary_game_display, str(team_detail[5].remaining_money), white, 'bahnschrift', 840, 580, 70)
    display_text.display_text(summary_game_display, str(team_detail[5].total_players), white, 'bahnschrift', 1030, 580, 70)
    display_text.display_text(summary_game_display, str(team_detail[5].foreign), white, 'bahnschrift', 1190, 580, 70)

    display_text.display_text(summary_game_display, "PK", white, 'bahnschrift', 420, 670, 70)
    display_text.display_text(summary_game_display, str(team_detail[6].remaining_money), white, 'bahnschrift', 840, 670, 70)
    display_text.display_text(summary_game_display, str(team_detail[6].total_players), white, 'bahnschrift', 1030, 670, 70)
    display_text.display_text(summary_game_display, str(team_detail[6].foreign), white, 'bahnschrift', 1190, 670, 70)

    display_text.display_text(summary_game_display, "RR", white, 'bahnschrift', 420, 750, 70)
    display_text.display_text(summary_game_display, str(team_detail[7].remaining_money), white, 'bahnschrift', 840, 750, 70)
    display_text.display_text(summary_game_display, str(team_detail[7].total_players), white, 'bahnschrift', 1030, 750, 70)
    display_text.display_text(summary_game_display, str(team_detail[7].foreign), white, 'bahnschrift', 1190, 750, 70)


def summary_loop(team_detail):
    dumped = False
    mixer.music.load("music/IPL 2020 Background Music Emotional Music -- মায়াপয়েন্ট -- IPL Cricket --.mp3")
    mixer.music.play()
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        summary_game_display.blit(background_page_1, (0, 0))
        if team_detail == None:
            team_detail = []
            team_detail.append(team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
        is_back = False
        is_back = pygane_button.button(summary_game_display, "Back", 20, 20, 100, 40, red, light_blue, 'back_from_summary')
        if is_back == True:
            mixer.music.stop()
            return
        title(team_detail)
        pygame.display.update()


