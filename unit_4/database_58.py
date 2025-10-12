import mysql.connector as mysql

# Connect to MySQL server
conn = mysql.connect(host="localhost",user="root",password="")

# Create a cursor object
cursor = conn.cursor()

# Execute SQL command to show databases
cursor.execute("SHOW DATABASES")

# Print all existing databases
print("List of Databases:")
for db in cursor:
    print(db[0])

# Close the connection
conn.close()
