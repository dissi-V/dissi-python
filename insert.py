import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (11, 'FAITH',18,134000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12, 'MARK',23,234000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13, 'JANE',31,150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14, 'JOHN',38,250000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (15, 'ALLAN',43,554000.00)")


conn.commit()
print("Records inserted successfully")
conn.close()