import pygame
import sys
import display_text
import pygane_button
import sqlite3
from pygame import mixer
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/laptop_display.jpg')
team_players_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("IPL Auction Game")
black = (0, 0, 0)
yellow = (237, 234, 52)
dark_red = (191, 34, 34)
red = (237, 21, 21)
light_blue = (21, 237, 219)
light_b = (21, 212, 237)
white = (0, 0, 0)
pink = (240, 22, 196)


def get_from_sql():
    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM csk_players"
    cursor.execute(command)
    csk_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM mi_players"
    cursor.execute(command)
    mi_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM rcb_players"
    cursor.execute(command)
    rcb_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM kkr_players"
    cursor.execute(command)
    kkr_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM srh_players"
    cursor.execute(command)
    srh_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM dc_players"
    cursor.execute(command)
    dc_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM pk_players"
    cursor.execute(command)
    pk_team = cursor.fetchall()
    con.commit()
    con.close()

    con = sqlite3.connect("IPL_AUCTION.db")
    cursor = con.cursor()
    command = "SELECT * FROM rr_players"
    cursor.execute(command)
    rr_team = cursor.fetchall()
    con.commit()
    con.close()

    teams = []
    teams.append(csk_team)
    teams.append(mi_team)
    teams.append(rcb_team)
    teams.append(kkr_team)
    teams.append(srh_team)
    teams.append(dc_team)
    teams.append(pk_team)
    teams.append(rr_team)
    return teams


def display_values(current_team, teams):
    if current_team == 'csk':
        players = teams[0]
    elif current_team == 'mi':
        players = teams[1]
    elif current_team == 'rcb':
        players = teams[2]
    elif current_team == 'kkr':
        players = teams[3]
    elif current_team == 'srh':
        players = teams[4]
    elif current_team == 'dc':
        players = teams[5]
    elif current_team == 'pk':
        players = teams[6]
    elif current_team == 'rr':
        players = teams[7]
    batsman_x = 420
    batsman_y = 205
    allrounder_x = 600
    allrounder_y = 205
    wk_x = 780
    wk_y = 205
    spin_x = 960
    spin_y = 205
    fast_x = 1140
    fast_y = 205
    for p in players:
        if p[4] == "Batsman":
            display_text.display_text(team_players_display, str(p[1].capitalize()), white, "freesansbold.ttf", batsman_x, batsman_y, 30)
            batsman_y += 30
        if p[4] == "Allrounder":
            display_text.display_text(team_players_display, str(p[1].capitalize()), white, "freesansbold.ttf", allrounder_x, allrounder_y, 30)
            allrounder_y += 30
        if p[4] == "wk/Batsman":
            display_text.display_text(team_players_display, str(p[1].capitalize()), white, "freesansbold.ttf", wk_x, wk_y, 30)
            wk_y += 30
        if p[4] == "Spin_Bowler":
            display_text.display_text(team_players_display, str(p[1].capitalize()), white, "freesansbold.ttf", spin_x, spin_y, 30)
            spin_y += 30
        if p[4] == "Fast_Bowler":
            display_text.display_text(team_players_display, str(p[1].capitalize()), white, "freesansbold.ttf", fast_x, fast_y, 30)
            fast_y += 30


def team_players_display_loop(myteam):
    mixer.music.load("music/IPL 2020 Background Music Emotional Music -- মায়াপয়েন্ট -- IPL Cricket --.mp3")
    mixer.music.play()
    current_team = myteam
    teams = get_from_sql()
    dumped = False
    while not dumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        team_players_display.blit(background_page_1, (0, 0))
        #default_values()
        is_back = pygane_button.button(team_players_display, "Back", 20, 20, 100, 40, red, light_blue, 'back_from_summary')
        if is_back == True:
            mixer.music.stop()
            return
        if current_team == 'csk':
            button_aa(team_players_display, "CSK", 336, 20, 108, 30, light_blue, light_blue, 'CSK')
        else:
            csk_select = button_aa(team_players_display, "CSK", 336, 20, 108, 30, red, light_blue, 'CSK')
            if csk_select == 'csk':
                current_team = 'csk'

        if current_team == 'mi':
            button_aa(team_players_display, "MI", 448, 20, 108, 30, light_blue, light_blue, 'MI')
        else:
            mi_select = button_aa(team_players_display, "MI", 448, 20, 108, 30, red, light_blue, 'MI')
            if mi_select == 'mi':
                current_team = 'mi'

        if current_team == 'rcb':
            button_aa(team_players_display, "RCB", 560, 20, 108, 30, light_blue, light_blue, 'RCB')
        else:
            rcb_select = button_aa(team_players_display, "RCB", 560, 20, 108, 30, red, light_blue, 'RCB')
            if rcb_select == 'rcb':
                current_team = 'rcb'

        if current_team == 'kkr':
            button_aa(team_players_display, "KKR", 672, 20, 108, 30, light_blue, light_blue, 'KKR')
        else:
            kkr_select = button_aa(team_players_display, "KKR", 672, 20, 108, 30, red, light_blue, 'KKR')
            if kkr_select == 'kkr':
                current_team = 'kkr'

        if current_team == 'srh':
            button_aa(team_players_display, "SRH", 784, 20, 108, 30, light_blue, light_blue, 'SRH')
        else:
            srh_select = button_aa(team_players_display, "SRH", 784, 20, 108, 30, red, light_blue, 'SRH')
            if srh_select == 'srh':
                current_team = 'srh'

        if current_team == 'dc':
            button_aa(team_players_display, "DC", 896, 20, 108, 30, light_blue, light_blue, 'DC')
        else:
            dc_select = button_aa(team_players_display, "DC", 896, 20, 108, 30, red, light_blue, 'DC')
            if dc_select == 'dc':
                current_team = 'dc'

        if current_team == 'pk':
            button_aa(team_players_display, "PK", 1008, 20, 108, 30, light_blue, light_blue, 'PK')
        else:
            pk_select = button_aa(team_players_display, "PK", 1008, 20, 108, 30, red, light_blue, 'PK')
            if pk_select == 'pk':
                current_team = 'pk'

        if current_team == 'rr':
            button_aa(team_players_display, "RR", 1120, 20, 108, 30, light_blue, light_blue, 'RR')
        else:
            rr_select = button_aa(team_players_display, "RR", 1120, 20, 108, 30, red, light_blue, 'RR')
            if rr_select == 'rr':
                current_team = 'rr'
        display_values(current_team, teams)
        pygame.display.update()


def button_aa(game_display, msg, x, y, w, h, ic, ac, action=None):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        display_text.display_text(game_display, str(msg), black, "freesansbold.ttf", x + (w/2), y + (h/2), 20)
        if (click[0] == 1) and (action != None):
            if action == "quit":
                pygame.quit()
                quit()
                sys.exit()
                #game_loop()
            elif action == "CSK":
                return 'csk'
            elif action == "MI":
                return 'mi'
            elif action == "RCB":
                return 'rcb'
            elif action == "KKR":
                return 'kkr'
            elif action == "SRH":
                return 'srh'
            elif action == "DC":
                return 'dc'
            elif action == "PK":
                return 'pk'
            elif action == "RR":
                return 'rr'

    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))
        display_text.display_text(game_display, str(msg), black, "freesansbold.ttf", x + (w/2), y + (h/2), 20)
        return 'no'

