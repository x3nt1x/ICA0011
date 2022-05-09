"""All MySQL scripts combined into a single Python script."""
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
)

cursor = mydb.cursor()


# Script 1: Create a Database
cursor.execute("CREATE DATABASE mydatabase")


# Script 2: Check if Database Exists
cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database)


# Script 3: Connect to a Database
cursor.close()
mydb.close()

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

cursor = mydb.cursor()


# Script 4: Create a Table
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Script 5: Check if Table Exists
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


# Script 6: Set a Primary Key
cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# Script 7: Insert Multiple Rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, "was inserted.")


# Script 8: Select From a Table
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for customer in result:
    print(customer)


# Script 9: Drop a Table if Exist
sql = "DROP TABLE IF EXISTS customers"
cursor.execute(sql)
