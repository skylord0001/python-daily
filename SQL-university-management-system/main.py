import sqlite3

# Connect to the database (creates a new file named 'university.db' if it doesn't exist)
conn = sqlite3.connect('university.db')

"""
conn = mysql.connector.connect(
    host='your_mysql_host',
    user='your_mysql_user',
    password='your_mysql_password',
    database='your_database'
)
"""
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_details (
        employee_id INTEGER PRIMARY KEY,
        address TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
        UNIQUE (employee_id)
    )
''')

# Create
def add_student(name):
    try:
        cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Student '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

def add_course(title):
    try:
        cursor.execute('INSERT INTO courses (title) VALUES (?)', (title,))
        conn.commit()
        print(f"Course '{title}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")

def enroll_student(student_id, course_id):
    try:
        # Check if the enrollment already exists
        cursor.execute('SELECT * FROM enrollments WHERE student_id = ? AND course_id = ?', (student_id, course_id))
        existing_enrollment = cursor.fetchone()

        if not existing_enrollment:
            cursor.execute('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
            conn.commit()
            print(f"Enrollment for student_id {student_id} and course_id {course_id} added successfully.")
        else:
            print(f"Enrollment for student_id {student_id} and course_id {course_id} already exists.")
    except sqlite3.Error as e:
        print(f"Error enrolling student: {e}")

def add_employee(name):
    try:
        cursor.execute('INSERT INTO employees (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Employee '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding employee: {e}")

def add_employee_details(employee_id, address):
    try:
        cursor.execute('INSERT INTO employee_details (employee_id, address) VALUES (?, ?)', (employee_id, address))
        conn.commit()
        print(f"Employee details for employee_id {employee_id} added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding employee details: {e}")

# Read
def get_students():
    try:
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
        return []

def get_courses():
    try:
        cursor.execute('SELECT * FROM courses')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching courses: {e}")
        return []

def get_enrollments():
    try:
        cursor.execute('SELECT * FROM enrollments')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching enrollments: {e}")
        return []

def get_employees():
    try:
        cursor.execute('SELECT * FROM employees')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching employees: {e}")
        return []

def get_employee_details():
    try:
        cursor.execute('SELECT * FROM employee_details')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching employee details: {e}")
        return []

# Update
def update_student_name(student_id, new_name):
    try:
        cursor.execute('UPDATE students SET name = ? WHERE student_id = ?', (new_name, student_id))
        conn.commit()
        print(f"Student with student_id {student_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating student name: {e}")

def update_employee_details_address(employee_id, new_address):
    try:
        cursor.execute('UPDATE employee_details SET address = ? WHERE employee_id = ?', (new_address, employee_id))
        conn.commit()
        print(f"Employee details for employee_id {employee_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating employee details address: {e}")

# Delete
def delete_student(student_id):
    try:
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        conn.commit()
        print(f"Student with student_id {student_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")

def delete_employee(employee_id):
    try:
        cursor.execute('DELETE FROM employees WHERE employee_id = ?', (employee_id,))
        conn.commit()
        print(f"Employee with employee_id {employee_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting employee: {e}")

# Example Usage
add_student('John Doe')
add_student('Jane Doe')

add_course('Introduction to Programming')
add_course('Database Management')

enroll_student(1, 1)
enroll_student(1, 2)
enroll_student(2, 2)

add_employee('Alice Smith')
add_employee_details(1, '123 Main St')

print("\nBefore Update and Delete:")
print("Students:")
print(get_students())

print("Courses:")
print(get_courses())

print("Enrollments:")
print(get_enrollments())

print("Employees:")
print(get_employees())

print("Employee Details:")
print(get_employee_details())

# Update
update_student_name(1, 'John Updated')
update_employee_details_address(1, '456 New St')

# Delete
delete_student(2)
delete_employee(1)

print("\nAfter Update and Delete:")
print("Students:")
print(get_students())

print("Employees:")
print(get_employees())

# Close the connection
conn.close()
