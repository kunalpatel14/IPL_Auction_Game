import pygame
import display_text
import sys
import right_screen
import team_class
import time
pygame.init()
clock = pygame.time.Clock()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/1_auction_hall.jpg')
team_detail = []
team_detail.append(team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))


def countdown(game_display, x, y, h, col):
    countd = True
    while countd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_display.blit(background_page_1, (0, 0))
        right_screen.right_screen(game_display, team_detail)
        display_text.display_text(game_display, "3", col,  'arialblack', x, y, h)
        pygame.display.update()
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 130)
        converter.setProperty('volume', 1)
        converter.say("3")
        converter.runAndWait()
        clock.tick(1)

        game_display.blit(background_page_1, (0, 0))
        right_screen.right_screen(game_display, team_detail)
        display_text.display_text(game_display, "2", col, 'arialblack', x, y, h)
        pygame.display.update()
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 130)
        converter.setProperty('volume', 1)
        converter.say("2")
        converter.runAndWait()

        clock.tick(1)

        game_display.blit(background_page_1, (0, 0))
        right_screen.right_screen(game_display, team_detail)
        display_text.display_text(game_display, "1", col, 'arialblack', x, y, h)
        pygame.display.update()
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 130)
        converter.setProperty('volume', 1)
        converter.say("1")
        converter.runAndWait()
        clock.tick(1)

        game_display.blit(background_page_1, (0, 0))
        right_screen.right_screen(game_display, team_detail)
        display_text.display_text(game_display, "GO!!", col, 'arialblack', x, y, h)
        pygame.display.update()
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 130)
        converter.setProperty('volume', 1)
        converter.say("And lets go")
        converter.runAndWait()
        clock.tick(1)
        countd = False
        return


