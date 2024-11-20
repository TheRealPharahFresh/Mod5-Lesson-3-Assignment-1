import mysql.connector
from mysql.connector import Error

def connect_database():

    db_name = "FitnessCenter"
    user = "root"
    password = "Godswill150"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connected to MySQL database successfully")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None