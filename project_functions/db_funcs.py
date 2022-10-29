import sqlite3

# Creates a database and creates the table


def enter_to_db(data):
    con = sqlite3.connect("../../test.db")
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tweets (sentence text, number of generation integer, date_last_created_text, 
    length)''')
    cursor.execute("INSERT INTO tweets VALUES" + str(data))
    con.commit()
    con.close()

# returns the oid for the last entry to the database


def search_db(name):
    con = sqlite3.connect("../../test.db")
    cursor = con.cursor()
    cursor.execute("SELECT oid, date_last_created_text FROM tweets WHERE sentence=?", (name,))
    temp = cursor.fetchone()
    return temp

# returns the average length of sentences in the database


def average_len():
    con = sqlite3.connect("../../test.db")
    cursor = con.cursor()
    cursor.execute("SELECT avg(length) From tweets")
    temp = cursor.fetchone()
    return temp
