import sqlite3  # import in python no need to install mySQL

connection = sqlite3.connect("Project.db") # Create database one time only
con = connection.cursor()

# Create table one time only
que = """CREATE TABLE GirlsProject ( 
rfid INTEGER PRIMARY KEY, 
StudentName VARCHAR(20), 
MobileNO varchar(30),
Stop VARCHAR(30), 
BusNo CHAR(1), 
PicupTime VARCHAR
);"""
con.execute(que)

# add some data in table here sql commands sent in string all other things same
sql_command = """INSERT INTO GirlsProject VALUES (123456, "New Student",+932327777777, "KSK", "6", '7:27');"""
con.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123457, "New Student",+932327777777, "KSK", "6", '7:27');"""
con.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123458, "New Student",+932327777777, "KSK", "6", '7:27');"""
con.execute(sql_command)

sql_command = """INSERT INTO GirlsProject VALUES (123459, "New Student",+932327777777, "KSK", "6", '7:27');"""
con.execute(sql_command)

connection.commit()
connection.close()


# extrac data may be this impelement in other file
connection = sqlite3.connect("Project.db") # give relative or absolute path acc to location
con = connection.cursor()

con.execute("SELECT * FROM girlsproject")
print("fetchall:")
result = con.fetchall()
for r in result:
    print(r)
