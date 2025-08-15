<<<<<<< HEAD
import mysql.connector
from mysql.connector import Error

try:
    # Establish connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="customer_segmentation"
    )

    if conn.is_connected():
        print("✅ Connected to MySQL database")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customers")

        rows = cursor.fetchall()

        # Print all rows
        for row in rows:
            print(row)

except Error as e:
    print(f"❌ Error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("🔒 Connection closed")
=======
import mysql.connector  # Import MySQL connector module

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",          # Database server address
    user="root",               # Database username
    password="root",           # Database password
    database="customer_segmentation"  # Target database name
)

cursor = conn.cursor()  # Create a cursor object to interact with the database

cursor.execute("SELECT * FROM Customers")  # Execute a SQL query to select all records from the Customers table

# Fetch all rows returned by the query and iterate through each row
for row in cursor.fetchall():
    print(row)  # Print the current row (a tuple representing a customer record)

conn.close()  # Close the connection to free resources
>>>>>>> 91e291e1bad2f3e8455a1f28add62bea0b24712a
