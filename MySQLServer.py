import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # SQL statement to create the database (with IF NOT EXISTS to avoid error if it exists)
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        
        # Execute the query to create the database
        cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        # Handle specific error messages
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid credentials provided!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist!")
        else:
            print(f"Failed to connect or create database: {err}")
    
    finally:
        # Ensure that the cursor and connection are closed after the operation
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
