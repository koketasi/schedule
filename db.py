import sqlite3
database='database.db'

def create_schedule_table():
    con=sqlite3.connect(database)
    con.execute('CREATE TABLE IF NOT EXISTS schedule1(date,event)')
    con.close()