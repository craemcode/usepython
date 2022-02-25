import sqlite3

conn = sqlite3.connect('./data/drugs.db')

c = conn.cursor() #create cursor

# create table

#c.execute("""CREATE TABLE customers (
#    first_name text,
#    email text)
#    """
#    )

#many_customers = [
#    ('zack','cripz@gmail.com'),
#    ('jack','jack@gmail.com'),
#    ('pack','pack@gmail.com'), 
#]

#c.executemany("INSERT INTO customers VALUES (?,?)", many_customers)

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(f'{item[0]} : {item[1]}')

print('Command executed successfully!')

conn.commit()
conn.close()