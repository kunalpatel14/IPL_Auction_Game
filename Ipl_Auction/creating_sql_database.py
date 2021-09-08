import sqlite3
import pandas as pd


def create_database():
    data = pd.read_excel(r'D:\Python course\python projects\IPL_Auction\data\AUCTION_LIST.xlsx')
    col = ['Player_Id', 'set_no', 'first_name', 'country', 'foreign_code', 'specialism', 'right_left', 's_code', 'ipl_matches', 'other_matches', 'Runs', 'Batting_avg', 'Batting_strikeRate', 'Bowling_wickets', 'Bowling_avg', 'Bowling_economy', 'Prev_ipl_team', 'IPL_team_code', 'Base_price', 'Sold_Unsold', 'IPL_team_buyed_player']
    df = pd.DataFrame(data, columns=col)

    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()

    sql_command = """CREATE TABLE IF NOT EXISTS IPL_PLAYER_LIST
                    (  Player_Id                INTEGER PRIMARY KEY,
                        set_no                  INTEGER,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        ipl_matches             INTEGER,
                        other_matches           INTEGER,
                        Runs                    INTEGER,
                        Batting_avg             FLOAT(6,2),
                        Batting_strikeRate      FLOAT(6,2),
                        Bowling_wickets         INTEGER,
                        Bowling_avg             FLOAT(6,2),
                        Bowling_economy         FLOAT(6,2),
                        Prev_ipl_team           VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_Unsold             BOOL,
                        IPL_team_buyed_player   INTEGER);"""
    cursor.execute(sql_command)
    conn.commit()
    conn.close()
    return
