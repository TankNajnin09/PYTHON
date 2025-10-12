import mysql.connector as mysql

# connect to MySQL database
conn = mysql.connect(host='localhost', database='world', user='root', password='')

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# read GR No (or any key) from user
grno = int(input("Enter GR No to delete: "))

# prepare SQL query string to delete a row
query = "DELETE FROM student WHERE grno = %s"

try:
    # execute the SQL query using execute() method
    cursor.execute(query, (grno,))
    
    # check if any row was deleted
    if cursor.rowcount > 0:
        conn.commit()
        print("✅ 1 row deleted successfully!")
    else:
        print("❌ grno is not available...")

except mysql.Error as e:
    conn.rollback()
    print("❌ Error while deleting record:", e)

# close connection
cursor.close()
conn.close()
