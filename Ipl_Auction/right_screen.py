import pygame
import sys

import display_text
black = (0, 0, 0)
yellow = (237, 234, 52)
dark_red = (191, 34, 34)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
white = (255, 255, 255)
pink = (240, 22, 196)
pygame.init()


def right_screen(game_display, team_detail):
    display_text.display_text(game_display, "Teams", yellow, 'bahnschrift', 1295, 250, 20)
    display_text.display_text(game_display, "Money", yellow, 'bahnschrift', 1378, 240, 10)
    display_text.display_text(game_display, "( CR )", yellow, 'bahnschrift', 1378, 257, 10)
    display_text.display_text(game_display, "Players", yellow, 'bahnschrift', 1425, 257, 10)
    display_text.display_text(game_display, "Total", yellow, 'bahnschrift', 1420, 240, 10)
    display_text.display_text(game_display, "Players", yellow, 'bahnschrift', 1465, 257, 10)
    display_text.display_text(game_display, "Foreign", yellow, 'bahnschrift', 1465, 240, 10)

    display_text.display_text(game_display, "CSK", white, 'bahnschrift', 1280, 278, 15)
    display_text.display_text(game_display, str(team_detail[0].remaining_money), white, 'bahnschrift', 1380, 278, 15)
    display_text.display_text(game_display, str(team_detail[0].total_players), white, 'bahnschrift', 1425, 278, 15)
    display_text.display_text(game_display, str(team_detail[0].foreign), white, 'bahnschrift', 1465, 278, 15)

    display_text.display_text(game_display, "MI", white, 'bahnschrift', 1274, 298, 15)
    display_text.display_text(game_display, str(team_detail[1].remaining_money), white, 'bahnschrift', 1380, 298, 15)
    display_text.display_text(game_display, str(team_detail[1].total_players), white, 'bahnschrift', 1425, 298, 15)
    display_text.display_text(game_display, str(team_detail[1].foreign), white, 'bahnschrift', 1465, 298, 15)

    display_text.display_text(game_display, "RCB", white, 'bahnschrift', 1280, 318, 15)
    display_text.display_text(game_display, str(team_detail[2].remaining_money), white, 'bahnschrift', 1380, 318, 15)
    display_text.display_text(game_display, str(team_detail[2].total_players), white, 'bahnschrift', 1425, 318, 15)
    display_text.display_text(game_display, str(team_detail[2].foreign), white, 'bahnschrift', 1465, 318, 15)

    display_text.display_text(game_display, "KKR", white, 'bahnschrift', 1280, 337, 15)
    display_text.display_text(game_display, str(team_detail[3].remaining_money), white, 'bahnschrift', 1380, 337, 15)
    display_text.display_text(game_display, str(team_detail[3].total_players), white, 'bahnschrift', 1425, 337, 15)
    display_text.display_text(game_display, str(team_detail[3].foreign), white, 'bahnschrift', 1465, 337, 15)

    display_text.display_text(game_display, "SRH", white, 'bahnschrift', 1280, 356, 15)
    display_text.display_text(game_display, str(team_detail[4].remaining_money), white, 'bahnschrift', 1380, 356, 15)
    display_text.display_text(game_display, str(team_detail[4].total_players), white, 'bahnschrift', 1425, 356, 15)
    display_text.display_text(game_display, str(team_detail[4].foreign), white, 'bahnschrift', 1465, 356, 15)

    display_text.display_text(game_display, "DC", white, 'bahnschrift', 1277, 374, 15)
    display_text.display_text(game_display, str(team_detail[5].remaining_money), white, 'bahnschrift', 1380, 374, 15)
    display_text.display_text(game_display, str(team_detail[5].total_players), white, 'bahnschrift', 1425, 374, 15)
    display_text.display_text(game_display, str(team_detail[5].foreign), white, 'bahnschrift', 1465, 374, 15)

    display_text.display_text(game_display, "PK", white, 'bahnschrift', 1275, 393, 15)
    display_text.display_text(game_display, str(team_detail[6].remaining_money), white, 'bahnschrift', 1380, 393, 15)
    display_text.display_text(game_display, str(team_detail[6].total_players), white, 'bahnschrift', 1425, 393, 15)
    display_text.display_text(game_display, str(team_detail[6].foreign), white, 'bahnschrift', 1465, 393, 15)

    display_text.display_text(game_display, "RR", white, 'bahnschrift', 1277, 413, 15)
    display_text.display_text(game_display, str(team_detail[7].remaining_money), white, 'bahnschrift', 1380, 413, 15)
    display_text.display_text(game_display, str(team_detail[7].total_players), white, 'bahnschrift', 1425, 413, 15)
    display_text.display_text(game_display, str(team_detail[7].foreign), white, 'bahnschrift', 1465, 413, 15)