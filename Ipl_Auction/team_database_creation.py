import sqlite3


def team_database_creation():
    conn = sqlite3.connect('IPL_AUCTION.db')
    cursor = conn.cursor()

    sql_command = """CREATE TABLE IF NOT EXISTS csk_players
                    (   Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command)
    conn.commit()

    sql_command1 = """CREATE TABLE IF NOT EXISTS mi_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command1)
    conn.commit()

    sql_command2 = """CREATE TABLE IF NOT EXISTS rcb_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command2)
    conn.commit()

    sql_command3 = """CREATE TABLE IF NOT EXISTS kkr_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command3)
    conn.commit()

    sql_command4 = """CREATE TABLE IF NOT EXISTS srh_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command4)
    conn.commit()

    sql_command5 = """CREATE TABLE IF NOT EXISTS dc_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command5)
    conn.commit()

    sql_command6 = """CREATE TABLE IF NOT EXISTS pk_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command6)
    conn.commit()

    sql_command7 = """CREATE TABLE IF NOT EXISTS rr_players
                    (  Player_Id                INTEGER PRIMARY KEY,
                        first_name              TEXT(50),
                        country                 TEXT(50),
                        foreign_code            INTEGER,
                        specialism              TEXT(50),
                        right_left              INTEGER,
                        s_code                  INTEGER,
                        new_ipl_team            VARCHAR(200),
                        IPL_team_code           INTEGER,
                        Base_price              INTEGER,
                        Sold_price              INTEGER);"""
    cursor.execute(sql_command7)
    conn.commit()

    sql_command8 = """CREATE TABLE IF NOT EXISTS my_history
                        ( csk       INTEGER,
                          mi        INTEGER,
                          rcb       INTEGER,
                          kkr       INTEGER,
                          srh       INTEGER,
                          dc        INTEGER,
                          pk        INTEGER,
                          rr        INTEGER);"""
    cursor.execute(sql_command8)
    conn.commit()
    conn.commit()
    conn.close()

