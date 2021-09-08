import pygame
import sys
import os.path
import countdown
import team_database_creation
import creating_sql_database
import inserting_values_to_database
import sqlite3
pygame.init()
clock = pygame.time.Clock()
black = (0, 0, 0)
light_blue = (21, 237, 219)
red = (245, 16, 0)
background_page_2 = pygame.image.load("photo/1_auction_hall.jpg")
team_detail = []
import team_class
team_detail.append(team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))


def start_my_game(myteam, game_display):
    if not os.path.isfile("IPL_AUCTION.db"):
        creating_sql_database.create_database()
        inserting_values_to_database.inserting_values_to_data()
        team_database_creation.team_database_creation()
    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM my_history")
    con.commit()
    cursor.execute("INSERT INTO my_history VALUES (0,0,0,0,0,0,0,0) ")
    con.commit()
    cursor.execute("DELETE FROM csk_players")
    cursor.execute("DELETE FROM mi_players")
    cursor.execute("DELETE FROM rcb_players")
    cursor.execute("DELETE FROM kkr_players")
    cursor.execute("DELETE FROM srh_players")
    cursor.execute("DELETE FROM dc_players")
    cursor.execute("DELETE FROM pk_players")
    cursor.execute("DELETE FROM rr_players")
    cursor.execute('UPDATE IPL_PLAYER_LIST SET Sold_Unsold = 0')
    cursor.execute('UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 0')
    con.commit()
    if myteam == 'csk':
        command = "UPDATE my_history SET csk = 1"
        cursor.execute(command)
        con.commit()
    elif myteam == 'mi':
        command = "UPDATE my_history SET mi = 1"
        cursor.execute(command)
    elif myteam == 'rcb':
        command = "UPDATE my_history SET rcb = 1"
        cursor.execute(command)
    elif myteam == 'kkr':
        command = "UPDATE my_history SET kkr = 1"
        cursor.execute(command)
    elif myteam == 'srh':
        command = "UPDATE my_history SET srh = 1"
        cursor.execute(command)
    elif myteam == 'dc':
        command = "UPDATE my_history SET dc = 1"
        cursor.execute(command)
    elif myteam == 'pk':
        command = "UPDATE my_history SET pk = 1"
        cursor.execute(command)
    elif myteam == 'rr':
        command = "UPDATE my_history SET rr = 1"
        cursor.execute(command)
    con.commit()
    con.close()
    countdown.countdown(game_display, 748.5, 350, 100, light_blue)
    game_display.blit(background_page_2, (0, 0))
    import right_screen
    right_screen.right_screen(game_display, team_detail)
    pygame.display.update()
    import pyttsx3
    converter = pyttsx3.init()
    converter.setProperty('rate', 160)
    converter.setProperty('volume', 1)
    import display_text
    display_text.display_text(game_display, "Welcome to IPL Auction Game", light_blue, "arialblack", 748.5, 280, 30)
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('Rules For the Auction', True, red)
    game_display.blit(img1, (490, 320))
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('1. Every Team should Buy Minimum 18 Players', True, light_blue)
    game_display.blit(img1, (490, 360))
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('   and Maximum 25 Players.', True, light_blue)
    game_display.blit(img1, (490, 380))
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('2. Every team Can Buy Maximum 8 Foreign Players.', True, light_blue)
    game_display.blit(img1, (490, 410))
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('3. Each Team can use maximum of 9000 L', True, light_blue)
    game_display.blit(img1, (490, 440))
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render('    i.e 90 Cr For Buying a Players.', True, light_blue)
    game_display.blit(img1, (490, 460))
    pygame.display.update()
    converter.say("Ladies and gentleman, Please Welcome to, IPL auction Game")
    converter.say("Lets First see the rules of the Auction")
    converter.say("Every team should buy minimum 18 players and maximum 25 players")
    converter.say("Every team Can Buy Maximum 8 Foreign Players.")
    converter.say("Each Team can use maximum of 9000 Lakhs, That is 90 cr, for buying a players.")
    converter.say("Now Lets start the game with the first player in the auction")
    clock.tick(0.2)
    converter.runAndWait()
    return
