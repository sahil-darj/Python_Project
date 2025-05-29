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
