import mysql.connector as mysql

def update_rows(grno):
    try:
        # Connect to MySQL database
        conn = mysql.connect(host='localhost',database='world',user='root',password='')
        cursor = conn.cursor()

        # Check if grno exists first
        cursor.execute("SELECT * FROM student WHERE grno = %s", (grno,))
        record = cursor.fetchone()

        if record:
            # If record found, update std to 'BSC'
            query = "UPDATE student SET std = %s WHERE grno = %s"
            cursor.execute(query, ('BSC', grno))
            conn.commit()
            print("✅ 1 row updated successfully!")
        else:
            print("❌ grno is not available")

    except mysql.Error as e:
        print("Error:", e)
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ---- Main Part ----
X = int(input("Enter grno: "))
update_rows(X)
