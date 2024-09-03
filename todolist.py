import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create a table to store the tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY AUTOINCREMENT,
    task text NOT NULL,
    completed integer NOT NULL DEFAULT 0
)
""")

# Function to add a task
def add_task(task):
    cursor.execute("""
    INSERT INTO tasks (task)
    VALUES (?)
    """, (task,))
    conn.commit()
    print("Task added successfully.")

# Function to edit a task
def edit_task(id, task):
    cursor.execute("""
    UPDATE tasks
    SET task = ?
    WHERE id = ?
    """, (task, id))
    conn.commit()
    print("Task updated successfully.")

# Function to mark a task as complete
def complete_task(id):
    cursor.execute("""
    UPDATE tasks
    SET completed = 1
    WHERE id = ?
    """, (id,))
    conn.commit()
    print("Task completed.")

# Function to display all tasks
def display_tasks():
    cursor.execute("""
    SELECT * FROM tasks
    """)
    tasks = cursor.fetchall()
    for task in tasks:
        print(task[0], task[1], "Completed" if task[2] else "Incomplete")

# Add a tasks
add_task("Bench Press")
add_task("Deadlift")
add_task("Squat")
add_task("Dip")
add_task("Pull Up")

# Edit a task
edit_task(1, "Bench Press 100 KG")
edit_task(2, "Deadlift 100 KG")
edit_task(3, "Squat 100 KG")
edit_task(4, "Dip 80 KG")
edit_task(5, "Pull Up 50 KG")

# Mark a task as complete
complete_task(1)
complete_task(2)
complete_task(3)
complete_task(4)



# Display all tasks
display_tasks()

# Commit the changes and close the connection
conn.commit()
conn.close()
