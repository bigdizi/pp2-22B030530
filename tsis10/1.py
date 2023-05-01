import psycopg2 

con = psycopg2.connect("dbname=bigdizi user=bigdizi password=neuer2014")

cur = con.cursor()

print("database version")
cur.execute("select * from club join player on club_id = player.player_id")

db_version = cur.fetchone()
print(db_version)

cur.close()