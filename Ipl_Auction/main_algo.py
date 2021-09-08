
import sqlite3
import math
import team_class
import calculate_point



"""team_detail = []
team_detail.append(team_class.TEAM("csk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 1))
team_detail.append(team_class.TEAM("mi", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rcb", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("kkr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("srh", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("dc", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("pk", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))
team_detail.append(team_class.TEAM("rr", 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0))"""


conn = sqlite3.connect('IPL_AUCTION.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM IPL_PLAYER_LIST')

result = cursor.fetchall()


def get_other_teams_for_players(row, team_detail):
    points = calculate_point.calculate_points(row[7], row[8], row[11], row[12], row[14], row[15])
    points = math.trunc(points)

    if points == -1:
        return (('rcb', 0),('srh',0))
    min_price = calculate_point.decide_min_price_by_points(points, row[18], row[7])
    min_price /= 100

    avail_slots = calculate_point.check_available_slots(team_detail, row[7], row[4])
    max_price = calculate_point.decide_max_team_wise(min_price, team_detail, avail_slots, row[18])

    team_containder = calculate_point.select_top_teams(max_price)
    return team_containder


"""for row in result:

    points = calculate_point.calculate_points(row[7], row[8], row[11], row[12], row[14], row[15])
    points = math.trunc(points)

    if points == -1:
        continue
    min_price = calculate_point.decide_min_price_by_points(points, row[18], row[7])
    min_price /= 100

    avail_slots = calculate_point.check_available_slots(team_detail, row[7], row[4])
    max_price = calculate_point.decide_max_team_wise(min_price, team_detail, avail_slots, row[18])

    team_containder = calculate_point.select_top_teams(max_price)

    teams_buyed = calculate_point.buy_player(team_containder)
    if teams_buyed == None:
        continue
    team_detail = calculate_point.update_record(team_detail, teams_buyed, row[7], row[4])
    buying_of_each_team.update_main_record(row, teams_buyed[0],teams_buyed[1])
    #print(row[0], row[2], points, teams_buyed[0], teams_buyed[1])

for k in team_detail:
    print(k.name, k.total_players, round(k.remaining_money,2), k.foreign , k.br, k.bl, k.sra, k.sla, k.fra, k.fla, k.fr, k.fl, k.s, k.wk)
    
#buying_of_each_team.print_record()
"""