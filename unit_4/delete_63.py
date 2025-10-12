import mysql.connector

# Step 1: Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # 🔹 Replace with your MySQL password if required
    database="dbStudent"
)

cursor = conn.cursor()

# Step 2: Ask user which record to delete
student_id = int(input("Enter Student ID to delete: "))

# Step 3: Delete query
delete_query = "DELETE FROM tblStudInfo WHERE student_id = %s"

# Step 4: Execute and commit changes
cursor.execute(delete_query, (student_id,))
conn.commit()

# Step 5: Confirmation message
if cursor.rowcount > 0:
    print(f"\n✅ Record with Student ID {student_id} deleted successfully!")
else:
    print(f"\n⚠️ No record found with Student ID {student_id}.")

# Step 6: Close connection
cursor.close()
conn.close()
