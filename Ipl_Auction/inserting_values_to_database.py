import sqlite3
import mysql.connector
import pandas as pd

def inserting_values_to_data():
    data = pd.read_excel(r'D:\Python course\python projects\IPL_Auction\data\AUCTION_LIST.xlsx')
    col = ['Player_Id', 'set_no', 'first_name', 'country', 'foreign_code', 'specialism', 'right_left', 's_code', 'ipl_matches', 'other_matches', 'Runs', 'Batting_avg', 'Batting_strikeRate', 'Bowling_wickets', 'Bowling_avg', 'Bowling_economy', 'Prev_ipl_team', 'IPL_team_code', 'Base_price', 'Sold_Unsold', 'IPL_team_buyed_player']
    df = pd.DataFrame(data, columns=col)

    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()
    command = ("DELETE FROM IPL_PLAYER_LIST")
    cursor.execute(command)
    conn.commit()
    for (row, rs) in df.iterrows():
        Player_Id = int(rs[0])
        set_no = int(rs[1])
        first_name = str(rs[2])
        country = str(rs[3])
        foreign_code = int(rs[4])
        specialism = str(rs[5])
        right_left = int(rs[6])
        s_code = int(rs[7])
        ipl_matches = int(rs[8])
        other_matches = int(rs[9])
        Runs = int(rs[10])
        Batting_avg = float(rs[11])
        Batting_strikeRate = float(rs[12])
        Bowling_wickets = int(rs[13])
        Bowling_avg = float(rs[14])
        Bowling_economy = float(rs[15])
        Prev_ipl_team = str(rs[16])
        IPL_team_code = int(rs[17])
        Base_price = int(rs[18])
        Sold_Unsold = int(rs[19])
        IPL_team_buyed_player = int(rs[20])
        query = "insert into IPL_PLAYER_LIST values(" + str(Player_Id) + "," + str(set_no) + ",'" + first_name + "','" + country + "'," + str(foreign_code) + ",'" + specialism + "'," + str(right_left) + "," + str(s_code) + "," + str(ipl_matches) + "," + str(other_matches) + "," + str(Runs) + "," + str(Batting_avg) + "," + str(Batting_strikeRate) + "," + str(Bowling_wickets) + "," + str(Bowling_avg) + "," + str(Bowling_economy) + ",'" + str(Prev_ipl_team) + "'," + str(IPL_team_code) + "," + str(Base_price) + "," + str(Sold_Unsold) + "," + str(IPL_team_buyed_player) + ");"
        cursor.execute(query)
        conn.commit()
    conn.commit()
    conn.close()