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
