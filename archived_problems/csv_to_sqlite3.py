import sqlite3

connection = sqlite3.connect('csvdata.db')
c = connection.cursor()

c.execute("""CREATE TABLE users (
pk INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(32),
email VARCHAR(64),
country VARCHAR(32)
);""")
c.execute("""CREATE TABLE phones (
pk INTEGER PRIMARY KEY AUTOINCREMENT,
p1 INTEGER,
p2 INTEGER,
p3 INTEGER
);""")
data = []
with open('employees.csv', 'r') as f:
    rows = f.readlines()
    rows = list(map(lambda x:x.strip(),rows))
    for row in rows:
        row = row.split(',')
        data.append(row)

for lists in data:
    c.execute("INSERT INTO users(name,email,country) VALUES('{}','{}','{}')".format(lists[0],lists[4],lists[5]))
    c.execute("INSERT INTO phones(p1,p2,p3) VALUES('{}','{}','{}')".format(lists[1],lists[2],lists[3]))

connection.commit()
c.close()
connection.close()