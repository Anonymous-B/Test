import sqlite3 #import in python no need to install mySQL
connection = sqlite3.connect("company.db")
dbcon = connection.cursor()

query = """
CREATE TABLE if not exists GirlsProject ( 
rfid INTEGER PRIMARY KEY, 
StudentName VARCHAR(20), 
MobileNO = varchar(30),
Stop VARCHAR(30), 
BusNo CHAR(1), 
PicupTime VARCHAR
);"""

dbcon.execute(query)

def insertStudent(rfid,name,mob,stop,busno,pictime):
    return str.format


sql_command = """INSERT INTO GirlsProject VALUES (123456, "New Student",+932327777777, "KSK", "6", '7:27');"""
dbcon.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123456, "New Student",+932327777777, "KSK", "6", '7:27');"""
dbcon.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123456, "New Student",+932327777777, "KSK", "6", '7:27');"""
dbcon.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123456, "New Student",+932327777777, "KSK", "6", '7:27');"""
dbcon.execute(sql_command)



# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()

connection = sqlite3.connect("company.db")

dbcon = connection.cursor()

dbcon.execute("SELECT * FROM employee")
print("fetchall:")
result = dbcon.fetchall()
for r in result:
    print(r)
dbcon.execute("SELECT * FROM employee")
print("\nfetch one:")
res = dbcon.fetchone()
print(res)
