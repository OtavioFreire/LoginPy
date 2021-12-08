import sqlite3

#Conexão e criação do db
connection =  sqlite3.connect('LoginPY/Users.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Names TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Passwords TEXT NOT NULL
    );""")

print("CONNECTION OKAY")