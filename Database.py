import sqlite3  # import in python no need to install mySQL

connection = sqlite3.connect("Project.db") # Create database one time only
con = connection.cursor()

# Create table one time only
que = """CREATE TABLE GirlsProject ( 
rfid INTEGER PRIMARY KEY, 
StudentName Integer, 
MobileNO Integer,
Stop Integer
);"""

con.execute(que)

for i in range(101):
    format_str = """INSERT INTO GirlsProject VALUES ({first}, {second},{third},"{forth}");"""
    sql_command = format_str.format(first=i+300, second=i+3000, third=i+30000, forth=i+300000)
    con.execute(sql_command)
connection.commit()
connection.close()


# extrac data may be this impelement in other file
connection = sqlite3.connect("Project.db") # give relative or absolute path acc to location
con = connection.cursor()

con.execute("SELECT * FROM girlsproject")
result = con.fetchall()

for r in result:
    format_str = "Data is RFID {first} Name {second} AGE {third} BUS {forth}"
    s = format_str.format(first=r[0], second=r[1], third=r[2], forth=r[3])
    print(s)


