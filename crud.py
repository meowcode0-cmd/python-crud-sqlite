import sqlite3

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

conn.commit()
conn.close()


# ---------- CRUD FUNCTIONS ----------
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()
    conn.close()
    print("Student added\n")


def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Students ---")
    for row in rows:
        print(row)
    print()


def update_student():
    student_id = input("Enter ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    city = input("New city: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, city=?
        WHERE id=?
    """, (name, age, city, student_id))
    conn.commit()
    conn.close()
    print("Student updated\n")


def delete_student():
    student_id = input("Enter ID to delete: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted\n")


# ---------- MENU ----------
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Bye 👋")
        break
    else:
        print("Invalid choice\n")