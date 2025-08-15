

import mysql.connector  # Import the MySQL connector library

# Function to create the 'Customers' table
def create_table():
    # Establish connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",          # Hostname of the MySQL server
        user="root",               # MySQL username
        password="root",           # MySQL password
        database="customer_segmentation"  # Target database
    )
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands

    # SQL query to create the 'Customers' table if it doesn't exist already
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT PRIMARY KEY,       -- Unique ID for each customer
        Name VARCHAR(255),                -- Customer's name
        Age INT,                          -- Customer's age
        Annual_Income FLOAT,              -- Customer's income
        Spending_Score FLOAT,             -- Score based on spending behavior
        Purchase_Frequency INT,           -- Number of purchases made
        Region VARCHAR(100)               -- Region or area customer belongs to
    );
    """

    cursor.execute(create_table_query)  # Execute the table creation query
    conn.commit()                       # Commit the changes to the database

    print("Table Customers created or already exists.")  # Confirmation message

    cursor.close()  # Close the cursor
    conn.close()    # Close the database connection

# Entry point of the script
if __name__ == "__main__":
    create_table()
