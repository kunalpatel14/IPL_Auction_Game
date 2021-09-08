import sqlite3
import json
conn = sqlite3.connect('IPL_AUCTION.db')
cursor = conn.cursor()

lion = [1,'virat kohli', 'India', 0,'Batsman', 1, 1, 'csk', 1, 200, 1700]

"""cursor.execute('UPDATE IPL_PLAYER_LIST SET Sold_Unsold = 0')
cursor.execute('UPDATE IPL_PLAYER_LIST SET IPL_team_buyed_player = 0')
result = cursor.fetchall()
for row in result:
    print(row)"""

cursor.execute("SELECT * FROM csk_players")
r = cursor.fetchall()
print('csk', r)
conn.commit()
cursor.execute("SELECT * FROM mi_players")
r = cursor.fetchall()
print('mi', r)
conn.commit()
cursor.execute("SELECT * FROM rcb_players")
r = cursor.fetchall()
print('rcb', r)
conn.commit()
cursor.execute("SELECT * FROM kkr_players")
r = cursor.fetchall()
print('kkr', r)
conn.commit()
cursor.execute("SELECT * FROM srh_players")
r = cursor.fetchall()
print('srh', r)
conn.commit()
cursor.execute("SELECT * FROM dc_players")
r = cursor.fetchall()
print('dc', r)
conn.commit()
cursor.execute("SELECT * FROM pk_players")
r = cursor.fetchall()
print('pk', r)
conn.commit()
cursor.execute("SELECT * FROM rr_players")
r = cursor.fetchall()
print('rr', r)
conn.commit()



cursor.execute("SELECT * FROM my_history")
result = cursor.fetchall()
print(result)
conn.commit()
cursor.execute("SELECT * FROM rcb_players")
result2 = cursor.fetchall()
print(result2)

conn.commit()
conn.close()