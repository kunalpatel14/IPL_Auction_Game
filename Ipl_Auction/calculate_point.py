import math
import random
from collections import Counter


def calculate_points(s_code, ipl_mathces, Batting_avg, Batting_strikeRate, Bowling_avg, Bowling_economy):
    points = -1
    if s_code == 1 or s_code == 2 or s_code == 11:
        if Batting_avg == 0:
            return -1
        points = (Batting_avg + Batting_strikeRate) / Batting_avg
    elif (s_code < 7) and (s_code > 2):
        if Batting_avg == 0:
            return -1
        a = ((Batting_avg + Batting_strikeRate) / Batting_avg)
        b = ((Bowling_avg * 0.1) + (Bowling_economy * 0.1))
        if (a < 8) or (b < 5):
            points = min(a, b)
        else:
            return -1
    elif (s_code > 6) and (s_code < 11):
        points = (Bowling_avg * 0.1) + (Bowling_economy * 0.1)
    if ipl_mathces != 0:
        points -= 1
    else:
        points += 1

    if s_code == 1 or s_code == 2 or s_code == 11:
        if points < 8:
            return points
        else:
            return -1
    elif (s_code > 2) and (s_code < 7):
        if points < 8:
            return points
        else:
            return -1
    elif (s_code > 6) and (s_code < 11):
        if points < 5:
            return points
        else:
            return -1


def decide_min_price_by_points(points, Base_price ,s_code):
    if points <= 0:
        return -1
    if s_code ==1 or s_code == 2 or s_code == 11:
        if (points > 0) and (points <= 3):
            return Base_price * 6
        elif points == 4:
            return Base_price * 5
        elif points == 5:
            return Base_price * 3
        elif points == 6:
            return Base_price * 2
        elif points == 7:
            return Base_price * 1.5
        elif points == 8:
            return Base_price * 1
    else:
        if points == 1:
            return Base_price * 3
        elif points == 2:
            return Base_price * 3
        elif points == 3:
            return Base_price * 2
        elif points < 8 and (points >3):
            return Base_price * 1


max_price = {}


def decide_max_team_wise(min_price, team_detail, slots, base_price):

    for team in team_detail:
        if team.my_team != 1:
            if slots[team.name]:
                max_price_temp = 0
                if team.remaining_money < 0.2:
                    max_price[team.name] = 0
                    continue
                remaining_players = 25 - team.total_players
                if team.remaining_money / remaining_players <= 0.2:
                    max_price_temp = round(0.2, 0)
                    max_price[team.name] = max_price_temp
                    continue
                if remaining_players - 1 == 0:
                    max_price[team.name] = team.remaining_money
                else:
                    if remaining_players > 23:
                        max_price_temp = (team.remaining_money / 0.2) / (remaining_players - 1)
                    elif (remaining_players > 18) and (remaining_players < 24):
                        max_price_temp = (team.remaining_money / 0.3) / (remaining_players - 1)
                    elif (remaining_players > 15) and (remaining_players < 19):
                        max_price_temp = (team.remaining_money / 0.4) / (remaining_players - 1)
                    elif (remaining_players > 12) and (remaining_players < 16):
                        max_price_temp = (team.remaining_money / 0.5) / (remaining_players - 1)
                    elif (remaining_players > 5) and (remaining_players < 13):
                        max_price_temp = (team.remaining_money / 0.6) / (remaining_players - 1)
                    elif (remaining_players > 0) and (remaining_players < 6):
                        max_price_temp = (team.remaining_money / 0.7) / (remaining_players - 1)

                if min_price > max_price_temp:
                    if max_price_temp > base_price:
                        real_max_price = max_price_temp
                    else:
                        real_max_price = 0
                else:
                    real_max_price = (round(random.uniform(min_price, max_price_temp), 2)) * 100

                if real_max_price >= 200:
                    if real_max_price % 50 != 0:
                        real_max_price = real_max_price - (real_max_price % 50)
                else:
                    if real_max_price % 20 != 0:
                        real_max_price = real_max_price - (real_max_price % 20)
                max_price[team.name] = int(real_max_price)
            else:
                max_price[team.name] = 0
    return max_price


avail_slots = {}


def check_available_slots(team_detail, s_code, f_code):
    for team in team_detail:
        if team.my_team != 1:
            if team.total_players >= 25:
                avail_slots[team.name] = 0
            else:
                if f_code == 1:
                    if team.foreign < 8:
                        if s_code == 1 or s_code == 2:
                            if (team.br + team.bl) < 7:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                        elif s_code == 3 or s_code == 4:
                            if (team.sra + team.sla) < 3:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                        elif s_code == 5 or s_code == 6:
                            if (team.fra + team.fla) < 4:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                        elif s_code == 7 or s_code == 8:
                            if (team.fl + team.fr) < 4:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                        elif s_code == 9 or s_code == 10:
                            if team.s < 4:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                        elif s_code == 11:
                            if team.wk < 3:
                                avail_slots[team.name] = True
                            else:
                                avail_slots[team.name] = False
                    else:
                        avail_slots[team.name] = False
                else:
                    if s_code == 1 or s_code == 2:
                        if (team.br + team.bl) < 7:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
                    elif s_code == 3 or s_code == 4:
                        if (team.sra + team.sla) < 3:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
                    elif s_code == 5 or s_code == 6:
                        if (team.fra + team.fla) < 4:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
                    elif s_code == 7 or s_code == 8:
                        if (team.fl + team.fr) < 4:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
                    elif s_code == 9 or s_code == 10:
                        if team.s < 4:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
                    elif s_code == 11:
                        if team.wk < 3:
                            avail_slots[team.name] = True
                        else:
                            avail_slots[team.name] = False
    return avail_slots


def select_top_teams(price):
    n = random.randint(2, 4)
    top_4_count = Counter(price)
    top_4_list = top_4_count.most_common(n)
    teams_containder = []
    for i in top_4_list:
        teams_containder.append((i[0], i[1]))
    return teams_containder


def buy_player(teams):
    first_team_name = teams[0][0]
    second_team_name = teams[1][0]
    first_team_price = teams[0][1]
    second_team_price = teams[1][1]
    if first_team_price == 0:
        return
    if second_team_price < 200:
        if (second_team_price + 20) < first_team_price:
            buying_cost = second_team_price + 20
            buying_team = first_team_name
        else:
            buying_cost = second_team_price
            buying_team = second_team_name
    else:
        if (second_team_price + 50) < first_team_price:
            buying_cost = second_team_price + 50
            buying_team = first_team_name
        else:
            buying_cost = second_team_price
            buying_team = second_team_name

    return buying_team, buying_cost


def update_record(team_detail, team, s_code, f_code):
    team_name = team[0]
    price = round((team[1] / 100), 2)

    for row in team_detail:
        if row.name == team_name:
            if f_code == 1:
                row.foreign += 1
            row.remaining_money -= price
            row.total_players += 1
            if s_code == 1:
                row.br += 1
            elif s_code == 2:
                row.bl += 1
            elif s_code == 3:
                row.sra += 1
            elif s_code == 4:
                row.sla += 1
            elif s_code == 5:
                row.fra += 1
            elif s_code == 6:
                row.fla += 1
            elif s_code == 7:
                row.fr += 1
            elif s_code == 8:
                row.fl += 1
            elif s_code == 9 or s_code == 10:
                row.s += 1
            elif s_code == 11:
                row.wk += 1

    return team_detail


