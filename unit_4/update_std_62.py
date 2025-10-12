import mysql.connector

# Step 1: Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # 🔹 Replace with your MySQL password if any
    database="dbStudent"  # Connect directly to the student database
)

cursor = conn.cursor()

# Step 2: Take input from user for updating
student_id = int(input("Enter Student ID to update: "))

print("\nEnter new details for the student:")
student_name = input("Enter Student Name: ")
stream = input("Enter Stream: ")
college_name = input("Enter College Name: ")
contact_number = input("Enter Contact Number: ")
remarks = input("Enter Remarks: ")

# Step 3: Update query
update_query = """
UPDATE tblStudInfo 
SET student_name=%s, stream=%s, college_name=%s, contact_number=%s, remarks=%s 
WHERE student_id=%s
"""

# Step 4: Execute the update query
data = (student_name, stream, college_name, contact_number, remarks, student_id)
cursor.execute(update_query, data)
conn.commit()

# Step 5: Confirmation message
if cursor.rowcount > 0:
    print("\n✅ Student record updated successfully!")
else:
    print("\n⚠️ No record found with that Student ID.")

# Step 6: Close connection
cursor.close()
conn.close()
