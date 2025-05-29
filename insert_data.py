import mysql.connector  # To connect and interact with MySQL database
import pandas as pd      # To handle CSV data easily

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",          # Database server address
    user="root",               # Username
    password="root",           # Password
    database="customer_segmentation"  # Target database name
)

cursor = conn.cursor()  # Create a cursor object to execute SQL queries

# Load data from CSV file into a pandas DataFrame
df = pd.read_csv("customer_data.csv")

# Loop through each row in the DataFrame
for _, row in df.iterrows():
    # Insert data into the Customers table using parameterized query to prevent SQL injection
    cursor.execute("""
    INSERT IGNORE INTO Customers (CustomerID, Name, Age, Annual_Income, Spending_Score, Purchase_Frequency, Region) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))  # Convert row data to tuple matching table columns order

conn.commit()  # Commit the transaction to save all inserts permanently
cursor.close() # Close the cursor to free resources
conn.close()   # Close the database connection

print("Data inserted successfully!")  # Confirmation message
