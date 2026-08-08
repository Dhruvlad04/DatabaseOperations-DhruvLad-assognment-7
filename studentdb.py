from db_connection import get_connection

# Connect to PostgreSQL
conn = get_connection()
cur = conn.cursor()

print("=" * 50)
print("DATABASE OPERATIONS USING PYTHON")
print("=" * 50)

# Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);
""")
conn.commit()
print("✓ Table Created Successfully")

# Insert Default Record
cur.execute("""
INSERT INTO students(name, age, course)
VALUES(%s,%s,%s)
""", ("Dhruv", 20, "Python"))
conn.commit()
print("✓ Default Record Inserted")

# Dynamic Input
print("\nEnter Student Details")
name = input("Name: ")
age = int(input("Age: "))
course = input("Course: ")

cur.execute("""
INSERT INTO students(name, age, course)
VALUES(%s,%s,%s)
""", (name, age, course))
conn.commit()
print("✓ User Record Inserted")

# Fetch First Record
print("\nFirst Record:")
cur.execute("SELECT * FROM students")
print(cur.fetchone())

# SELECT with WHERE
course_name = input("\nEnter Course to Search: ")

cur.execute("""
SELECT * FROM students
WHERE course=%s
""", (course_name,))

rows = cur.fetchall()

print("\nMatching Records:")
for row in rows:
    print(row)

# Ask before truncating
choice = input("\nDo you want to truncate the table? (yes/no): ")

if choice.lower() == "yes":
    cur.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    conn.commit()
    print("✓ Table Truncated")
else:
    print("✓ Table Not Truncated")

cur.close()
conn.close()

print("\nConnection Closed Successfully.")
