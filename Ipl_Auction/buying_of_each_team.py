import sqlite3


def update_main_record(player, new_team, price):
    conn = sqlite3.connect("IPL_AUCTION.db")
    cursor = conn.cursor()
    player_id = player[0]
    player_name = player[2]
    player_country = player[3]
    player_foreign_code = player[4]
    player_spe = player[5]
    player_right_left = player[6]
    player_s_code = player[7]
    new_ipl_team = new_team
    player_base_price = player[18]
    player_price = price
    if new_team == "csk":
        player_ipl_team_code = 1
        sql_command = "INSERT INTO csk_players(Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "mi":
        player_ipl_team_code = 2
        sql_command = "INSERT INTO mi_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "rcb":
        player_ipl_team_code = 3
        sql_command = "INSERT INTO rcb_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price)  VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "kkr":
        player_ipl_team_code = 4
        sql_command = "INSERT INTO kkr_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price)VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "srh":
        player_ipl_team_code = 5
        sql_command = "INSERT INTO srh_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "dc":
        player_ipl_team_code = 6
        sql_command = "INSERT INTO dc_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "pk":
        player_ipl_team_code = 7
        sql_command = "INSERT INTO pk_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return
    if new_team == "rr":
        player_ipl_team_code = 8
        sql_command = "INSERT INTO rr_players (Player_Id,first_name ,country,foreign_code,specialism,right_left,s_code,new_ipl_team,IPL_team_code,Base_price,Sold_price) VALUES (?,?,?,?,?,?,?,?,?,?,?) "
        record = (player_id, player_name, player_country, player_foreign_code, player_spe, player_right_left, player_s_code, new_ipl_team, player_ipl_team_code, player_base_price, player_price)
        cursor.execute(sql_command,record)
        conn.commit()
        conn.close()
        return


def print_record():
    conn = sqlite3.connect("IPL_AUCTION.db")
    cursor = conn.cursor()
    print("csk Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM csk_players")
    result = cursor.fetchall()
    money = 0
    c=0
    for r in result:
        print(r)
        c +=1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n \n mi Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM mi_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\nrcb Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM rcb_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\nkkr Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM kkr_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\nsrh Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM srh_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\ndc Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM dc_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\npk Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM pk_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))

    print("\n\nrr Players")
    cursor.execute("SELECT player_id,first_name,Base_price,Sold_price FROM rr_players")
    result = cursor.fetchall()
    money = 0
    c = 0
    for r in result:
        print(r)
        c += 1
        money += r[3]
    print("Total Players Brought in Auction = " + str(c))
    print("Total Price Spend in Auction = " + str(money))
    conn.commit()
    conn.close()
    return


