import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kidicarus1@",
    database="menagerie"
)

cursor = mydb.cursor()
cursor.execute("SELECT name, birth, MONTH(birth) FROM pet ;")

for pet in cursor:
    print(pet)

"""
cursor = mydb.cursor()
cursor.execute("SELECT * FROM pet")
myresult = cursor.fetchall()

for x in myresult:
    print(x)


"""


"""
cursor = mydb.cursor()
records = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)"

values = [
    ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04'),
    ('Claws', 'Gwen', 'cat', 'm', '1994-03-17'),
    ('Buffy', 'Harold', 'dog', 'f', '1989-05-13'),
    ('Fang', 'Benny', 'dog', 'm', '1990-08-27'),
    ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1996-07-29'),
    ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11'),
    ('Whistler', 'Gwen', 'bird', '', '1997-12-09'),
    ('Slim', 'Benny', 'snake', 'm', '1996-04-29'),
    ('Puffball', 'Diane', 'hamster', 'f', '1999-03-30')
]

cursor = mydb.cursor(records, values)

"""

# cursor.execute("SELECT * FROM customers")
# print(cursor.fetchall())
# print(cursor.execute(cursor))


"""

# get cursor object
cursor = mydb.cursor()
# execute your query
cursor.execute("DESCRIBE pet")
# fetch all the matching rows
result = cursor.fetchall()
# loop through the rows
for row in result:
    print(row)


"""

"""
cursor = mydb.cursor()
cursor.execute("SELECT * FROM pet")
result = cursor.fetchall()

for x in result:
    print(x)

"""

"""
cursor = mydb.cursor()
cursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")

for pet in cursor:
    print(pet)
"""

"""


"""

"""
curser = mydb.cursor()
curser.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)")
curser.execute("SELECT * FROM pet")
result = curser.fetchall()
for row in result:
    print(row)
"""

"""
cursor = mydb.cursor()
databases = "show databases"
cursor.execute(databases)
for (databases) in cursor:
    print(databases[0])
"""

"""
cursor = mydb.cursor()
cursor.execute("DROP DATABASE menagerie")
"""

# print(mydb)
