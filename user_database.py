import sqlite3

#Dette ligger globalt så vi undgår at genbruge kode flere gange
con = sqlite3.connect('user_data.db', check_same_thread=False)
cur = con.cursor()


#Her får vi table names fra user_data.db som indeholder achievements for hver bruger. 
def get_user_tables():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = cur.fetchall()
    return [table[0] for table in tables]


#Her får vi data altså columns og rows fra et specifikt table.
def get_table_data(table_name):
    cur.execute(f"SELECT * FROM {table_name}")
    columns = [description[0] for description in cur.description]
    rows = cur.fetchall()
    return columns, rows

def createUserTable():
    # NAME DESCRITOPN COMPLETED
    Tablename = input("Please confirm which user is being updated: ")
    cur.execute(f"CREATE TABLE IF NOT EXISTS [{Tablename}] (uid INTEGER PRIMARY KEY, name TEXT, description TEXT, completed INTEGER, times INTEGER)")
    #cur.execute(f"INSERT INTO ")
    con.commit()

# def DropUserTable():
#     Tablename = input("Which table are you deleting? ")
#     print("Deleting table")
#     cur.execute(f"DROP TABLE {Tablename}")

#createUserTable()
#DropUserTable()