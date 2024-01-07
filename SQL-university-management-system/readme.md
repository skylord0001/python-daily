
# University Management System

This Python script demonstrates basic CRUD (Create, Read, Update, Delete) operations for managing a university database using SQLite. The script includes functions for adding students, courses, enrollments, employees, and employee details. It also provides functionality for reading, updating, and deleting records.

## Database Connection and Table Creation

```python
# Connect to the database (creates a new file named 'university.db' if it doesn't exist)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# (Similar CREATE TABLE statements for courses, enrollments, employees, and employee_details)
```
This section establishes a connection to the SQLite database named 'university.db' and creates tables for students, courses, enrollments, employees, and employee details if they don't already exist.

## Create Functions
```python
def add_student(name):
    try:
        cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Student '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

# (Similar functions for add_course, enroll_student, add_employee, and add_employee_details)

```
These functions handle the creation (INSERT) of new records in the respective tables. They use parameterized queries to avoid SQL injection and include error handling to catch any database-related issues.

## Read Functions
```python
def get_students():
    try:
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
        return []

# (Similar functions for get_courses, get_enrollments, get_employees, and get_employee_details)
```
These functions retrieve data (SELECT) from the respective tables. They execute SQL queries, fetch the results, and handle errors, returning the data or an empty list if an error occurs.

## Update Functions
```python
def update_student_name(student_id, new_name):
    try:
        cursor.execute('UPDATE students SET name = ? WHERE student_id = ?', (new_name, student_id))
        conn.commit()
        print(f"Student with student_id {student_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating student name: {e}")

# (Similar function for update_employee_details_address)
```
## Delete Functions
```python
def delete_student(student_id):
    try:
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        conn.commit()
        print(f"Student with student_id {student_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")

# (Similar function for delete_employee)
```

## Example Usage
```python
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
```
This part of the code demonstrates how to use the functions by adding sample data to the tables.

## Close the Connection
```python
# Close the connection
conn.close()
```
## Closing the Database Connection

If the connection (`conn.close()`) is not closed explicitly, it can lead to various issues:

- **Resource Leakage:** Each open connection consumes system resources. If connections are not closed, it can lead to resource leakage, potentially causing your application to run out of available resources over time.

- **Locking Issues:** In some database systems, not closing connections can lead to issues with locking. For example, other processes or applications might be prevented from accessing the database if there are open transactions on the same records.

- **Data Integrity:** Open connections can impact the consistency and integrity of your data. Changes made in one session might not be visible to other sessions until the connection is closed.

- **Performance:** Over time, having numerous open connections can impact the performance of your application and the database server.

To avoid these issues, it's a good practice to always close the database connection once you have finished using it. The `conn.close()` statement in your code is responsible for closing the connection to the SQLite database.

Here's where you should typically close the connection:

```python
# Example Usage
print("\nAfter Update and Delete:")
print("Students:")
print(get_students())

print("Employees:")
print(get_employees())

# Close the connection
conn.close()
```
This part of the code, at the end of the script, is where the connection is closed. Always make sure to include this statement to properly release resources and ensure the integrity and performance of your application.