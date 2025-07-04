import csv
import sqlite3

con = sqlite3.connect('jarvis.db')
cursor = con.cursor()

# Create system command table (for desktop apps)
# query = """
# CREATE TABLE IF NOT EXISTS sys_command(
#     id INTEGER PRIMARY KEY, 
#     name VARCHAR(100), 
#     path VARCHAR(1000)
# )
# """
# cursor.execute(query)

# Create web command table (for websites)
# query = """
# CREATE TABLE IF NOT EXISTS web_command(
#     id INTEGER PRIMARY KEY, 
#     name VARCHAR(100), 
#     url VARCHAR(1000)
# )
# """
# cursor.execute(query)

# Insert system commands (example paths - adjust to your PC paths)
# cursor.execute("INSERT INTO sys_command VALUES (null,'android studio','C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')")
# If your Android Studio path is different, update accordingly

# Insert web commands
# cursor.execute("INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')")
# cursor.execute("INSERT INTO web_command VALUES (null,'instagram','https://www.instagram.com/')")
# cursor.execute("INSERT INTO web_command VALUES (null,'discord','https://discord.com/')")

# con.commit()
# con.close()
# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 18]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts1.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # # Commit changes and close connection
# con.commit()
# # con.close()
# query = 'Prithivi'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])