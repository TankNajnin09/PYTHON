import mysql.connector

# Step 1: Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    database="dbStudent ",
    user="root",
    password=""
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS tblStudInfo (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    stream VARCHAR(50),
    college_name VARCHAR(100),
    contact_number VARCHAR(15),
    remarks VARCHAR(100)
)
"""
cursor.execute(create_table_query)
print("✅ Table 'tblStudInfo' created successfully (if not already exists).")

# Step 5: Insert student record
insert_query = """
INSERT INTO tblStudInfo (student_id, student_name, stream, college_name, contact_number, remarks)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Sample data entry (you can replace or take from user input)
student_data = (
    1, 
    "Najnin Tank", 
    "BCA", 
    "Kamani Science College", 
    "9876543210", 
    "Excellent Student"
)

cursor.execute(insert_query, student_data)
conn.commit()

print("✅ Student record inserted successfully!")

# Step 6: Close connection
cursor.close()
conn.close()
