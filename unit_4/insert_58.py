import mysql.connector as mysql

try:
    # Connect to MySQL
    conn = mysql.connect(
        host='localhost',
        database='world',
        user='root',
        password=''
    )
    cursor = conn.cursor()

    # Read data from user
    grno = int(input("Enter GR No: "))
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    std = input("Enter Standard: ")
    birth_date = input("Enter Birth Date (YYYY-MM-DD): ")

    # Use parameterized query for safety
    query = "INSERT INTO student (grno, name, address, std, birth_date) VALUES (%s, %s, %s, %s, %s)"
    values = (grno, name, address, std, birth_date)

    cursor.execute(query, values)
    conn.commit()

    print("✅ 1 row inserted successfully!")

except mysql.Error as e:
    print("❌ Error:", e)
    conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
