import pygame
import sys
import display_text
import pygane_button
import right_screen
import sqlite3
import main_algo
import team_class
import text_to_speech
from pygame import mixer
clock = pygame.time.Clock()
pygame.init()
display_width = 1500
display_height = 800
background_page_1 = pygame.image.load('photo/1_auction_hall_with_temp1.jpg')
background_page_2 = pygame.image.load('photo/1_auction_hall.jpg')
india_flag = pygame.image.load('photo/india_flag.png')
aus_flag = pygame.image.load('photo/aus_flag.jpg')
eng_flag = pygame.image.load('photo/eng_flag.jpg')
nz_flag = pygame.image.load('photo/nz_flag.jpg')
wi_flag = pygame.image.load('photo/wi_flag.jpg')
ban_flag = pygame.image.load('photo/bangladesh_flag.jpg')
afg_flag = pygame.image.load('photo/aug_flag.jpg')
sa_flag = pygame.image.load('photo/sa_flag.jpg')
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
first_time = 0
i = 0


def get_original_name(current_team):
    if current_team == 'csk':
        return 'Chennai super kings'
    elif current_team == 'mi':
        return 'mumbai indians'
    elif current_team == 'rcb':
        return 'royal challengers bangalore'
    elif current_team == 'kkr':
        return 'kolkata knight Riders'
    elif current_team == 'srh':
        return 'sunrisers hyderabad'
    elif current_team == 'dc':
        return 'delhi capitals'
    elif current_team == 'pk':
        return 'punjab kings'
    elif current_team == 'rr':
        return 'rajasthan royals'


def left_screen_unsold(player, team_detail, name, base_price):
    name = player[2]
    spec = player[5]
    ipl_matches = player[8]
    other_matches = player[9]
    runs = player[10]
    country = player[3]
    batting_avg = player[11]
    strike_rate = player[12]
    wickets = player[13]
    bowling_avg = player[14]
    economy = player[15]
    base_price = player[18]
    game_display.blit(background_page_1, (0, 0))
    update_values(name.capitalize(), spec, ipl_matches, other_matches, runs, batting_avg, strike_rate, wickets,
                  bowling_avg, economy, base_price, team_detail, country)
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render(str(name.capitalize()), True, black)
    font2 = pygame.font.SysFont('arialblack', 20)
    img2 = font2.render(str(base_price), True, black)
    game_display.blit(img1, (30, 240))
    game_display.blit(img2, (170, 240))

    font3 = pygame.font.SysFont('arialblack', 15)
    img3 = font3.render("UNSOLD", True, black)
    game_display.blit(img3, (35, 285))


def display_players_button(game_display, msg, x, y, w, h, ic, ac, myteam ,action=None):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
        if (click[0] == 1) and (action != None):
            if action == 'quit_icon':
                pygame.quit()
                quit()
                sys.exit()
            elif action == 'team_players':
                import team_players_buyed_display
                team_players_buyed_display.team_players_display_loop(myteam)
                return


def create_team_list(myteam):
    teams_name_list = ['csk', 'mi', 'rcb', 'kkr', 'srh', 'dc', 'pk', 'rr']
    team_detail = []
    i = 0
    for t_name in teams_name_list:
        con = sqlite3.connect("IPL_AUCTION.db")
        cursor = con.cursor()
        command = f"SELECT * FROM {t_name}_players"
        i += 1
        cursor.execute(command)
        result = cursor.fetchall()
        con.commit()
        con.close()
        print(result)
        total_players = 0
        br = 0
        bl = 0
        wk = 0
        sra = 0
        sla = 0
        fra = 0
        fla = 0
        fr = 0
        fl = 0
        s = 0
        fore = 0
        remaining_money = 90
        if len(result) == 0:
            if t_name == 'csk':
                if myteam == 'csk':
                    team_detail.append(
                        team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
            if t_name == 'mi':
                if myteam == 'mi':
                    team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'rcb':
                if myteam == 'rcb':
                    team_detail.append(
                        team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'kkr':
                if myteam == 'kkr':
                    team_detail.append(
                        team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'srh':
                if myteam == 'srh':
                    team_detail.append(
                        team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'dc':
                if myteam == 'dc':
                    team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'pk':
                if myteam == 'pk':
                    team_detail.append(team_class.TEAM("pk",90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))

            if t_name == 'rr':
                if myteam == 'rr':
                    team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
                else:
                    team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
        else:
            for r in result:
                if r[3] != 0:
                    fore += 1
                remaining_money -= (r[10]/100)
                remaining_money = round(remaining_money, 2)
                total_players += 1
                if r[6] == 1:
                    br += 1
                elif r[6] == 2:
                    bl += 1
                elif r[6] == 3:
                    sra += 1
                elif r[6] == 4:
                    sla += 1
                elif r[6] == 5:
                    fra += 1
                elif r[6] == 6:
                    fla += 1
                elif r[6] == 7:
                    fr += 1
                elif r[6] == 8:
                    fl += 1
                elif r[6] == 9 or r[6] == 10:
                    s += 1
                elif r[6] == 11:
                    wk += 1
            if t_name == 'csk':
                if myteam == 'csk':
                    team_detail.append(
                        team_class.TEAM("csk", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("csk", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))
            if t_name == 'mi':
                if myteam == 'mi':
                    team_detail.append(team_class.TEAM("mi", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(team_class.TEAM("mi", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'rcb':
                if myteam == 'rcb':
                    team_detail.append(
                        team_class.TEAM("rcb", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore,remaining_money, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("rcb", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'kkr':
                if myteam == 'kkr':
                    team_detail.append(
                        team_class.TEAM("kkr", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("kkr", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'srh':
                if myteam == 'srh':
                    team_detail.append(
                        team_class.TEAM("srh", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(
                        team_class.TEAM("srh", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'dc':
                if myteam == 'dc':
                    team_detail.append(team_class.TEAM("dc", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(team_class.TEAM("dc", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'pk':
                if myteam == 'pk':
                    team_detail.append(team_class.TEAM("pk",90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(team_class.TEAM("pk", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))

            if t_name == 'rr':
                if myteam == 'rr':
                    team_detail.append(team_class.TEAM("rr", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 1))
                else:
                    team_detail.append(team_class.TEAM("rr", 90, total_players, br, bl, wk, sra, sla, fra, fla, fr, fl, s, fore, remaining_money, 0))
    print(team_detail[7].remaining_money)
    return team_detail


def here_button(game_display, msg, x, y, w, h, ic, ac, action=None):
    global pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
        if (click[0] == 1) and (action != None):
            if action == "bid":
                return True
            if action == "skip_player":
                return True
        else:
            return False


def left_screen_sold(player, team_detail, name, base_price, current_team, current_price, sold_team=None, sold_price=-1):

    name = player[2]
    spec = player[5]
    ipl_matches = player[8]
    other_matches = player[9]
    runs = player[10]
    country = player[3]
    batting_avg = player[11]
    strike_rate = player[12]
    wickets = player[13]
    bowling_avg = player[14]
    economy = player[15]
    base_price = player[18]
    game_display.blit(background_page_1, (0, 0))
    update_values(name.capitalize(), spec, ipl_matches, other_matches, runs, batting_avg, strike_rate, wickets,
                  bowling_avg, economy, base_price, team_detail, country)
    """display_text.display_text(game_display, str(name), red, 'algerian', 132, 250, 20)
    display_text.display_text(game_display, "Sold to "+str(sold_team)+" For "+str(sold_price), red, 'algerian', 132, 300, 15)"""
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render(str(name.capitalize()), True, black)
    font2 = pygame.font.SysFont('arialblack', 20)
    img2 = font2.render(str(base_price), True, black)
    game_display.blit(img1, (30, 240))
    game_display.blit(img2, (170, 240))

    font3 = pygame.font.SysFont('arialblack', 15)
    img3 = font3.render("Sold", True, black)
    game_display.blit(img3, (35, 285))
    font4 = pygame.font.SysFont('arialblack', 15)
    img4 = font4.render("For", True, black)
    game_display.blit(img4, (35, 305))
    font4 = pygame.font.SysFont('arialblack', 30)
    img4 = font4.render(f"₹{str(sold_price)}", True, black)
    game_display.blit(img4, (120, 285))

    font5 = pygame.font.SysFont('arialblack', 20)
    img5 = font5.render("To :", True, black)
    game_display.blit(img5, (35, 360))

    font6 = pygame.font.SysFont('arialblack', 30)
    img6 = font6.render(str(sold_team), True, black)
    game_display.blit(img6, (100, 350))
    pygame.display.update()
    clock.tick(0.5)


def left_screen_per(name, base_price, current_team, current_price, sold_team = None, sold_price=-1):
    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render(str(name.capitalize()), True, black)
    """font2 = pygame.font.SysFont('arialblack', 20)
    img2 = font2.render(str(base_price), True, black)"""
    game_display.blit(img1, (30, 240))
    """game_display.blit(img2, (170, 240))"""

    font3 = pygame.font.SysFont('arialblack', 15)
    img3 = font3.render("Current", True, black)
    game_display.blit(img3, (35, 285))
    font4 = pygame.font.SysFont('arialblack', 15)
    img4 = font4.render("Bid", True, black)
    game_display.blit(img4, (35, 305))

    font5 = pygame.font.SysFont('arialblack', 20)
    img5 = font5.render("By :", True, black)
    game_display.blit(img5, (35, 360))


def left_screen(name, base_price, current_team, current_price, sold_team = None, sold_price=-1):

    font1 = pygame.font.SysFont('arialblack', 18)
    img1 = font1.render(str(name.capitalize()), True, black)
    game_display.blit(img1, (30, 240))

    font3 = pygame.font.SysFont('arialblack', 15)
    img3 = font3.render("Current", True, black)
    game_display.blit(img3, (35, 285))
    font4 = pygame.font.SysFont('arialblack', 15)
    img4 = font4.render("Bid", True, black)
    game_display.blit(img4, (35, 305))
    font4 = pygame.font.SysFont('arialblack', 30)
    img4 = font4.render(f"₹{str(current_price)}", True, black)
    game_display.blit(img4, (120, 285))

    font5 = pygame.font.SysFont('arialblack', 20)
    img5 = font5.render("By :", True, black)
    game_display.blit(img5, (35, 360))

    font6 = pygame.font.SysFont('arialblack', 30)
    img6 = font6.render(str(current_team), True, black)
    game_display.blit(img6, (100, 350))
    pygame.display.update()


def update_values(name, spec, ipl_matches, other_matches, runs, batting_avg, strike_rate, wickets, bowling_avg, economy, base_price, team_detail, country):
    if len(name) > 14:
        font1 = pygame.font.SysFont('arialblack', 15)
        img1 = font1.render(name, True, light_blue)
    else:
        font1 = pygame.font.SysFont('arialblack', 18)
        img1 = font1.render(name, True, light_blue)

    font2 = pygame.font.SysFont('arialblack', 15)
    img2 = font2.render(spec, True, light_blue)
    game_display.blit(img1, (680, 300))
    game_display.blit(img2, (680, 340))
    if ipl_matches != 0:
        display_text.display_text(game_display, "IPL Matches", white, 'bahnschrift', 945, 310, 15)
        display_text.display_text(game_display, str(ipl_matches), white, 'arialblack', 945, 340, 45)
    else:
        display_text.display_text(game_display, "Other Matches", white, 'bahnschrift', 945, 310, 15)
        display_text.display_text(game_display, str(other_matches), white, 'arialblack', 945, 340, 45)

    display_text.display_text(game_display, "Runs", black, 'arialblack', 705, 390, 15)
    display_text.display_text(game_display, "Average", black, 'arialblack', 795, 390, 15)
    display_text.display_text(game_display, "Strike Rate", black, 'arialblack', 885, 390, 15)

    display_text.display_text(game_display, str(runs), white, 'arialblack', 705, 418, 15)
    display_text.display_text(game_display, str(batting_avg), white, 'arialblack', 795, 418, 15)
    display_text.display_text(game_display, str(strike_rate), white, 'arialblack', 885, 418, 15)

    display_text.display_text(game_display, "Wickets", black, 'arialblack', 715, 447, 15)
    display_text.display_text(game_display, "Average", black, 'arialblack', 795, 447, 15)
    display_text.display_text(game_display, "Economy", black, 'arialblack', 885, 447, 15)

    display_text.display_text(game_display, str(wickets), white, 'arialblack', 705, 478, 15)
    display_text.display_text(game_display, str(bowling_avg), white, 'arialblack', 795, 478, 15)
    display_text.display_text(game_display, str(economy), white, 'arialblack', 885, 478, 15)

    display_text.display_text(game_display, "Base", black, 'bahnschrift', 525, 438, 20)
    display_text.display_text(game_display, "Price", black, 'bahnschrift', 525, 458, 20)
    display_text.display_text(game_display, str(base_price)+" L", black, 'arialblack', 605, 448, 25)
    game_display.blit(india_flag, (520, 320))
    if country == "India":
        game_display.blit(india_flag, (520, 320))
    elif country == "Aus":
        game_display.blit(aus_flag, (520, 320))
    elif country == "ENG":
        game_display.blit(eng_flag, (520, 320))
    elif country == "WI":
        game_display.blit(wi_flag, (520, 320))
    elif country == "SA":
        game_display.blit(sa_flag, (520, 320))
    elif country == "AFG":
        game_display.blit(afg_flag, (520, 320))
    elif country == "NZ":
        game_display.blit(nz_flag, (520, 320))
    elif country == "BAN":
        game_display.blit(ban_flag, (520, 320))
    right_screen.right_screen(game_display, team_detail)
    pygame.display.update()


def start_game_loop(myteam, my_price):
    global i
    appear_here_first_time = 0
    team_detail = create_team_list(myteam)
    finished = False
    while not finished:
        player = get_player_values()
        id = player[0]
        if id == 285:
            finished = True
        name = player[2]
        country = player[3]
        spec = player[5]
        s_code = player[7]
        ipl_matches = player[8]
        other_matches = player[9]
        runs = player[10]
        batting_avg = player[11]
        strike_rate = player[12]
        wickets = player[13]
        bowling_avg = player[14]
        economy = player[15]
        base_price = player[18]
        teams_containder = main_algo.get_other_teams_for_players(player, team_detail)
        game_display.blit(background_page_1, (0, 0))
        update_values(name.capitalize(), spec, ipl_matches, other_matches, runs, batting_avg, strike_rate, wickets,
                      bowling_avg, economy, base_price, team_detail, country)
        left_screen_per(name, base_price, "", base_price)
        pygame.display.update()
        mixer.init()
        if appear_here_first_time == 0:
            clock.tick(0.5)
            appear_here_first_time = 1
        text_to_speech.text_to_speech(f"Next Player is {name}")
        mixer.music.load(f"music/Next Player is {name}.wav")
        mixer.music.play()
        clock.tick(0.3)
        if s_code == 1:
            text_to_speech.text_to_speech(f"The Right Handed Batsman")
            mixer.music.load(f"music/The Right Handed Batsman.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 2:
            text_to_speech.text_to_speech(f"The Left Handed Batsman")
            mixer.music.load(f"music/The Left Handed Batsman.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 3:
            text_to_speech.text_to_speech(f"Leg Spinner Allrounder")
            mixer.music.load(f"music/Leg Spinner Allrounder.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 4:
            text_to_speech.text_to_speech(f"Off Spinner Allrounder")
            mixer.music.load(f"music/Off Spinner Allrounder.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 5:
            text_to_speech.text_to_speech(f"Right Arm fast Bowler Allrounder")
            mixer.music.load(f"music/Right Arm fast Bowler Allrounder.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 6:
            text_to_speech.text_to_speech(f"left arm fast Bowler Allrounder")
            mixer.music.load(f"music/left arm fast Bowler Allrounder.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 7:
            text_to_speech.text_to_speech(f"Right Arm Fast Bowler")
            mixer.music.load(f"music/Right Arm Fast Bowler.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 8:
            text_to_speech.text_to_speech(f"left Arm Fast Bowler")
            mixer.music.load(f"music/left Arm Fast Bowler.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 9:
            text_to_speech.text_to_speech(f"Leg spinner")
            mixer.music.load(f"music/Leg spinner.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 10:
            text_to_speech.text_to_speech(f"off spinner")
            mixer.music.load(f"music/off spinner.wav")
            mixer.music.play()
            #clock.tick(0.8)
        elif s_code == 11:
            text_to_speech.text_to_speech(f"wicket keeper batsman")
            mixer.music.load(f"music/wicket keeper batsman.wav")
            mixer.music.play()
            #clock.tick(0.8)
        mixer.music.stop()
        text_to_speech.text_to_speech(f"I am Looking For {base_price} lakh for {name}")
        mixer.music.queue(f"music/I am Looking For {base_price} lakh for {name}.wav")
        mixer.music.play()
        clock.tick(0.3)
        length = len(teams_containder)
        team1_name = ""
        team1_price = int()
        team2_name = ""
        team2_price = int()
        team3_name = ""
        team3_price = int()
        team4_name = myteam
        team4_price = int(my_price)
        current_team = ""
        sold_team = ""
        sold_price = -1
        buyed = 0
        current_price = int(base_price)
        is_my_bid = False
        team1_name = teams_containder[0][0]
        team1_price = int(teams_containder[0][1])
        team2_name = teams_containder[1][0]
        team2_price = int(teams_containder[1][1])
        if team1_price == 0 and team2_price == 0:
            no_team_involved = 0
        else:
            no_team_involved = 1
        if team1_price != 0 and team2_price == 0:
            team2_price = team1_price*0.6
            only_one_team = 0
        else:
            only_one_team = 1
        dumped = False
        counter = 0
        buyed_counter = 0
        while not dumped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            game_display.blit(background_page_1, (0, 0))
            update_values(name.capitalize(), spec, ipl_matches, other_matches, runs, batting_avg, strike_rate, wickets,
                          bowling_avg, economy, base_price, team_detail, country)
            own_bid = False
            skip_player = False
            skip_player = here_button(game_display, "hii", 40, 730, 230, 45, red, light_blue, 'skip_player')
            if skip_player == True:
                buyed = 1
                if no_team_involved == 0:
                    sold_price = 0
                    sold_team = ""
                elif team1_price >= team2_price:
                    if team2_price >= 200:
                        buyed = 1
                        sold_team = team1_name
                        sold_price = team2_price + 25
                    elif team2_price >= 100 and team2_price < 200:
                        buyed = 1
                        sold_team = team1_name
                        sold_price = team2_price + 10
                    elif team2_price < 100:
                        buyed = 1
                        sold_team = team1_name
                        sold_price = team2_price + 10
                elif team1_price < team2_price:
                    if team1_price >= 200:
                        buyed = 1
                        sold_team = team2_name
                        sold_price = team1_price + 25
                    elif team1_price >= 100 and team1_price < 200:
                        buyed = 1
                        sold_team = team2_name
                        sold_price = team1_price + 20
                    elif team1_price < 100:
                        buyed = 1
                        sold_team = team2_name
                        sold_price = team1_price + 25

            if current_price <= my_price:
                own_bid = here_button(game_display, "hii", 35, 630, 230, 65, red, light_blue, 'bid')
            if own_bid == True and current_team != myteam:
                is_my_bid = True
                if current_price >= 200:
                    if current_price + 25 <= my_price:
                        current_price = current_price + 25
                        current_team = myteam
                elif current_price < 200 and current_price >= 100:
                    if current_price + 20 <= my_price:
                        current_price = current_price + 10
                        current_team = myteam
                elif current_price < 100:
                    if current_price + 25 <= my_price:
                        current_price = current_price + 10
                        current_team = myteam
                full_team_name = get_original_name(current_team)
                text_to_speech.text_to_speech(f"{current_price} from {full_team_name}")
                mixer.music.load(f"music/{current_price} from {full_team_name}.wav")
                mixer.music.play()
                counter = 0
                left_screen(name, base_price, current_team, current_price)
            if current_price >= team1_price and current_team == myteam:
                buyed = 1
                sold_team = myteam
                sold_price = current_price
            if counter == 80:
                if no_team_involved == 0:
                    buyed = 1
                    sold_price = 0
                    sold_team = ""
            if no_team_involved == 1:
                if is_my_bid == True:
                    if counter == 80:
                        if buyed == 0:
                            list_l = bid_for_player(current_price, buyed, current_team, base_price, team1_name, team2_name,
                                                    team1_price, team2_price, myteam, my_price)
                            buyed = list_l[0]
                            current_price = list_l[1]
                            current_team = list_l[2]
                            if buyed == 1:
                                sold_price = list_l[3]
                                sold_team = list_l[4]
                        counter = 0
                        full_team_name = get_original_name(current_team)
                        text_to_speech.text_to_speech(f"{current_price} from {full_team_name}")
                        mixer.music.load(f"music/{current_price} from {full_team_name}.wav")
                        mixer.music.play()
                        left_screen(name, base_price, current_team, current_price)
                elif counter == 80:
                    if buyed == 0:
                        list_l = bid_for_player(current_price, buyed, current_team, base_price, team1_name, team2_name,
                                                team1_price, team2_price, myteam, my_price)
                        buyed = list_l[0]
                        current_price = list_l[1]
                        current_team = list_l[2]
                        if buyed == 1:
                            sold_price = list_l[3]
                            sold_team = list_l[4]
                    counter = 0
                    full_team_name = get_original_name(current_team)
                    text_to_speech.text_to_speech(f"{current_price} from {full_team_name}")
                    mixer.music.load(f"music/{current_price} from {full_team_name}.wav")
                    mixer.music.play()
                    left_screen(name, base_price, current_team, current_price)
            here_button(game_display, "hii", 40, 720, 240, 60, red, light_blue, 'skip_player')
            left_screen(name, base_price, current_team, current_price)
            #pygane_button.tranparent_button(game_display, "hii", 1080, 650, 180, 90, red, light_blue, team_detail, 'team_players' )
            display_players_button(game_display, "hii", 1080, 650, 180, 90, red, red, myteam, 'team_players')
            pygane_button.tranparent_button(game_display, "hii", 1258, 230, 240, 195, red, light_blue, team_detail, 'summary')
            pygane_button.tranparent_button(game_display, "hii", 36, 20, 50, 50, red, light_blue, team_detail, 'instruction_icon')
            pygane_button.tranparent_button(game_display, "hii", 1430, 1, 80, 70, red, light_blue, team_detail, 'quit_icon')
            pygane_button.tranparent_button(game_display, "hii", 1350, 1, 70, 70, red, light_blue, team_detail,'back_to_menu_icon')

            if buyed == 1:
                if sold_team == myteam:
                    my_price -= sold_price
                """if buyed_counter == 50:
                    text_to_speech.text_to_speech(f"I am selling the player")
                    mixer.music.load(f"music/I am selling the player.wav")
                    mixer.music.play()
                    clock.tick(0.3)"""
                if buyed_counter == 100:
                    if sold_price == 0:
                        left_screen_unsold(player, team_detail, name, base_price)
                        pygame.display.update()
                        text_to_speech.text_to_speech(f"{name} is Unsold")
                        mixer.music.load(f"music/{name} is Unsold.wav")
                        mixer.music.play()
                        clock.tick(0.1)
                    else:
                        left_screen_sold(player, team_detail, name, base_price, current_team, current_price, sold_team, sold_price)
                        full_team_name = get_original_name(sold_team)
                        text_to_speech.text_to_speech(f"{name} is sold to {sold_team} for {sold_price}")
                        mixer.music.load(f"music/{name} is sold to {sold_team} for {sold_price}.wav")
                        mixer.music.play()
                        clock.tick(0.3)
                    team_detail = update_buyed_player_list(player, sold_price, sold_team, team_detail)
                    dumped = True
                buyed_counter += 1
            pygame.display.update()
            counter += 1
    if finished == True:
        import team_players_buyed_display
        team_players_buyed_display.team_players_display_loop(myteam)
        import background_page_1
        background_page_1.background_1_loop()


def bid_for_player(current_price, buyed, current_team, base_price, team1_name, team2_name, team1_price, team2_price, myteam, my_price):
    sold_to_team = "none"
    sold_by_price = -1
    if current_price == base_price:
        current_price = base_price
        current_team = team1_name
    if current_team == team1_name:
        if current_price >= 200:
            if team2_price >= current_price + 25:
                current_team = team2_name
                current_price += 25
        elif current_price < 200 and current_price >= 100:
            if team2_price >= current_price + 10:
                current_team = team2_name
                current_price += 10
        elif current_price < 100:
            if team2_price >= current_price + 10:
                current_team = team2_name
                current_price += 10
        if current_team == team1_name:
            sold_to_team = str(current_team)
            sold_by_price = int(current_price)
            buyed = 1
    elif current_team == team2_name:
        if current_price >= 200:
            if team1_price >= current_price + 25:
                current_team = team1_name
                current_price += 25
        elif current_price < 200 and current_price >= 100:
            if team1_price >= current_price + 10:
                current_team = team1_name
                current_price += 10
        elif current_price < 100:
            if team1_price >= current_price + 10:
                current_team = team1_name
                current_price += 10
        if current_team == team2_name:
            sold_to_team = str(current_team)
            sold_by_price = int(current_price)
            buyed = 1
    elif current_team == myteam:
        if current_price >= 200:
            if team1_price >= current_price + 25:
                current_team = team1_name
                current_price += 25
        elif current_price < 200 and current_price >= 100:
            if team1_price >= current_price + 10:
                current_team = team1_name
                current_price += 10
        elif current_price < 100:
            if team1_price >= current_price + 10:
                current_team = team1_name
                current_price += 10
        if current_team == team2_name:
            sold_to_team = str(current_team)
            sold_by_price = int(current_price)
            buyed = 1
    if current_price >= team1_price and current_team == myteam:
        buyed = 1
        sold_by_price = current_price
        sold_to_team = myteam
    list_l = []
    list_l.append(buyed)
    list_l.append(current_price)
    list_l.append(current_team)
    if sold_by_price != -1:
        list_l.append(sold_by_price)
        list_l.append(sold_to_team)
    return list_l


def get_player_values():
    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()

    command = ("SELECT * FROM IPL_PLAYER_LIST WHERE Sold_Unsold = 0")
    cursor.execute(command)
    row = cursor.fetchall()
    conn.commit()
    conn.close()
    for r in row:
        name = r[2]
        spec = r[5]
        ipl_matches = r[8]
        other_matches = r[9]
        runs = r[10]
        batting_avg = r[11]
        strike_rate = r[12]
        wickets = r[13]
        bowling_avg = r[14]
        economy = r[15]
        base_price = r[18]
        break
    return r


def update_buyed_player_list(player, sold_price, sold_team, team_detail):
    id = player[0]
    s_code = player[7]
    price = round((sold_price /100),2)
    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()
    sql_command = f"UPDATE IPL_PLAYER_LIST SET Sold_Unsold = 1 WHERE Player_Id = {id}"
    cursor.execute(sql_command)
    conn.commit()
    conn.close()
    if sold_team == 'csk':
        team_detail[0].total_players += 1
        team_detail[0].remaining_money -= price
        round(team_detail[0].remaining_money)
        if player[4] == 1:
            team_detail[0].foreign += 1
        if player[7] == 1:
            team_detail[0].br += 1
        elif player[7] == 2:
            team_detail[0].bl += 1
        elif player[7] == 3:
            team_detail[0].sra += 1
        elif player[7] == 4:
            team_detail[0].sla += 1
        elif player[7] == 5:
            team_detail[0].fra += 1
        elif player[7] == 6:
            team_detail[0].fla += 1
        elif player[7] == 7:
            team_detail[0].fr += 1
        elif player[7] == 8:
            team_detail[0].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[0].s += 1
        elif player[7] == 11:
            team_detail[0].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 1 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'mi':
        team_detail[1].total_players += 1
        team_detail[1].remaining_money -= price
        round(team_detail[1].remaining_money)
        if player[4] == 1:
            team_detail[1].foreign += 1
        if player[7] == 1:
            team_detail[1].br += 1
        elif player[7] == 2:
            team_detail[1].bl += 1
        elif player[7] == 3:
            team_detail[1].sra += 1
        elif player[7] == 4:
            team_detail[1].sla += 1
        elif player[7] == 5:
            team_detail[0].fra += 1
        elif player[7] == 6:
            team_detail[1].fla += 1
        elif player[7] == 7:
            team_detail[1].fr += 1
        elif player[7] == 8:
            team_detail[1].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[1].s += 1
        elif player[7] == 11:
            team_detail[1].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 1 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'rcb':
        team_detail[2].total_players += 1
        team_detail[2].remaining_money -= price
        round(team_detail[2].remaining_money)
        if player[4] == 1:
            team_detail[2].foreign += 1
        if player[7] == 1:
            team_detail[2].br += 1
        elif player[7] == 2:
            team_detail[2].bl += 1
        elif player[7] == 3:
            team_detail[2].sra += 1
        elif player[7] == 4:
            team_detail[2].sla += 1
        elif player[7] == 5:
            team_detail[2].fra += 1
        elif player[7] == 6:
            team_detail[2].fla += 1
        elif player[7] == 7:
            team_detail[2].fr += 1
        elif player[7] == 8:
            team_detail[2].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[2].s += 1
        elif player[7] == 11:
            team_detail[2].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 3 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'kkr':
        team_detail[3].total_players += 1
        team_detail[3].remaining_money -= price
        round(team_detail[3].remaining_money)
        if player[4] == 1:
            team_detail[3].foreign += 1
        if player[7] == 1:
            team_detail[3].br += 1
        elif player[7] == 2:
            team_detail[3].bl += 1
        elif player[7] == 3:
            team_detail[3].sra += 1
        elif player[7] == 4:
            team_detail[3].sla += 1
        elif player[7] == 5:
            team_detail[3].fra += 1
        elif player[7] == 6:
            team_detail[3].fla += 1
        elif player[7] == 7:
            team_detail[3].fr += 1
        elif player[7] == 8:
            team_detail[3].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[3].s += 1
        elif player[7] == 11:
            team_detail[3].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 4 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'srh':
        team_detail[4].total_players += 1
        team_detail[4].remaining_money -= price
        round(team_detail[4].remaining_money)
        if player[4] == 1:
            team_detail[4].foreign += 1
        if player[7] == 1:
            team_detail[4].br += 1
        elif player[7] == 2:
            team_detail[4].bl += 1
        elif player[7] == 3:
            team_detail[4].sra += 1
        elif player[7] == 4:
            team_detail[4].sla += 1
        elif player[7] == 5:
            team_detail[4].fra += 1
        elif player[7] == 6:
            team_detail[4].fla += 1
        elif player[7] == 7:
            team_detail[4].fr += 1
        elif player[7] == 8:
            team_detail[4].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[4].s += 1
        elif player[7] == 11:
            team_detail[4].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 5 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'dc':
        team_detail[5].total_players += 1
        team_detail[5].remaining_money -= price
        round(team_detail[5].remaining_money)
        if player[4] == 1:
            team_detail[5].foreign += 1
        if player[7] == 1:
            team_detail[5].br += 1
        elif player[7] == 2:
            team_detail[5].bl += 1
        elif player[7] == 3:
            team_detail[5].sra += 1
        elif player[7] == 4:
            team_detail[5].sla += 1
        elif player[7] == 5:
            team_detail[5].fra += 1
        elif player[7] == 6:
            team_detail[5].fla += 1
        elif player[7] == 7:
            team_detail[5].fr += 1
        elif player[7] == 8:
            team_detail[5].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[5].s += 1
        elif player[7] == 11:
            team_detail[5].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 6 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    if sold_team == 'pk':
        team_detail[6].total_players += 1
        team_detail[6].remaining_money -= price
        round(team_detail[6].remaining_money)
        if player[4] == 1:
            team_detail[6].foreign += 1
        if player[7] == 1:
            team_detail[6].br += 1
        elif player[7] == 2:
            team_detail[6].bl += 1
        elif player[7] == 3:
            team_detail[6].sra += 1
        elif player[7] == 4:
            team_detail[6].sla += 1
        elif player[7] == 5:
            team_detail[6].fra += 1
        elif player[7] == 6:
            team_detail[6].fla += 1
        elif player[7] == 7:
            team_detail[6].fr += 1
        elif player[7] == 8:
            team_detail[6].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[6].s += 1
        elif player[7] == 11:
            team_detail[6].wk +=1
    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()
    sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 7 WHERE Player_Id = {id}"
    cursor.execute(sql_command)
    conn.commit()
    conn.close()

    if sold_team == 'rr':
        team_detail[7].total_players += 1
        team_detail[7].remaining_money -= price
        round(team_detail[7].remaining_money)
        if player[4] == 1:
            team_detail[7].foreign += 1
        if player[7] == 1:
            team_detail[7].br += 1
        elif player[7] == 2:
            team_detail[7].bl += 1
        elif player[7] == 3:
            team_detail[7].sra += 1
        elif player[7] == 4:
            team_detail[7].sla += 1
        elif player[7] == 5:
            team_detail[7].fra += 1
        elif player[7] == 6:
            team_detail[7].fla += 1
        elif player[7] == 7:
            team_detail[7].fr += 1
        elif player[7] == 8:
            team_detail[7].fl += 1
        elif player[7] == 9 or player[7] == 10:
            team_detail[7].s += 1
        elif player[7] == 11:
            team_detail[7].wk +=1
        conn = sqlite3.connect('IPL_AUCTION.db')
        cursor = conn.cursor()
        sql_command = f"UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 8 WHERE Player_Id = {id}"
        cursor.execute(sql_command)
        conn.commit()
        conn.close()

    import buying_of_each_team
    buying_of_each_team.update_main_record(player, sold_team, sold_price)
    return team_detail

