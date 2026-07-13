import numpy as np
from db import get_connection

try:
    # Connect to MySQL
    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------
    # Read students1
    # -----------------------------
    cursor.execute("SELECT * FROM students1")
    students1 = cursor.fetchall()

    students1_array = np.array(students1)

    print("\nStudents1 Data:")
    print(students1_array)

    # -----------------------------
    # Extract Marks
    # -----------------------------
    marks = students1_array[:, 3].astype(int)

    print("\nMarks Array:")
    print(marks)

    # -----------------------------
    # NumPy Operations
    # -----------------------------
    highest = np.max(marks)
    lowest = np.min(marks)
    average = np.mean(marks)

    print("\nHighest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Average Marks:", average)

    print("Above Average:", marks[marks > average])
    print("Below Average:", marks[marks < average])

    # -----------------------------
    # Read students2
    # -----------------------------
    cursor.execute("SELECT * FROM students2")
    students2 = cursor.fetchall()

    students2_array = np.array(students2)

    print("\nStudents2 Data:")
    print(students2_array)

    # -----------------------------
    # Concatenate Arrays
    # -----------------------------
    final_array = np.concatenate((students1_array, students2_array), axis=0)

    print("\nConcatenated Array:")
    print(final_array)

    # -----------------------------
    # Clear students3 (optional)
    # -----------------------------
    cursor.execute("DELETE FROM students3")

    # -----------------------------
    # Insert into students3
    # -----------------------------
    query = """
    INSERT INTO students3(id, name, course, marks)
    VALUES (%s, %s, %s, %s)
    """

    for row in final_array:
        cursor.execute(query, tuple(row))

    conn.commit()

    print("\nData inserted into students3 successfully.")

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")