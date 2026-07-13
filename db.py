import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anoosh@7799",
        database="numpy_demo"
    )