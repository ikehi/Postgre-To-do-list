import psycopg2

# Connect to the Postgres database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="1234"
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Create the 'todos' table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    task VARCHAR(255) NOT NULL
);
"""
cursor.execute(create_table_query)
conn.commit()

def add_task(task):
    insert_query = "INSERT INTO todo (task) VALUES (%s);"
    cursor.execute(insert_query, (task,))
    conn.commit()
    print("Task added successfully.")

def get_tasks():
    select_query = "SELECT * FROM todo;"
    cursor.execute(select_query)
    tasks = cursor.fetchall()
    print("Tasks:")
    for task in tasks:
        print(f"ID: {task[0]}, Task: {task[1]}")

def delete_task(task_id):
    delete_query = "DELETE FROM todo WHERE id = %s;"
    cursor.execute(delete_query, (task_id,))
    conn.commit()
    print("Task deleted successfully.")

# Add tasks to the To-Do List
add_task("Finsh test on bincom")
add_task("Finish class on bincom")
add_task("Tell bincom im done with the test")

# Get all tasks from the To-Do List
get_tasks()

# Delete a task from the To-Do List (provide the task ID)
delete_task(2)

# Get all tasks again to see the updated list
get_tasks()

# Close the cursor and the database connection
cursor.close()
conn.close()
