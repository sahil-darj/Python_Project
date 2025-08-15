import mysql.connector  # Import MySQL connector to interact with the database

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",       # Database host address
    user="root",            # Database username
    password="root",        # Database password
    database="customer_segmentation"  # Target database name
)

cursor = conn.cursor()  # Create cursor object to execute SQL queries

# Collect customer data from user input
customer_id = int(input("Enter Customer ID: "))           # Convert input to integer
name = input("Enter Name: ")                               # String input for name
age = int(input("Enter Age: "))                            # Integer input for age
annual_income = float(input("Enter Annual Income: "))      # Float input for income
spending_score = float(input("Enter Spending Score: "))   # Float input for spending score
purchase_frequency = int(input("Enter Purchase Frequency: "))  # Integer input for purchase frequency
region = input("Enter Region: ")                           # String input for region

# Prepare SQL INSERT query with placeholders for parameters
query = """
INSERT INTO Customers (CustomerID, Name, Age, Annual_Income, Spending_Score, Purchase_Frequency, Region) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Tuple of values to be inserted, matching the placeholders in query
values = (customer_id, name, age, annual_income, spending_score, purchase_frequency, region)

try:
    cursor.execute(query, values)  # Execute the query with provided values
    conn.commit()                  # Commit the transaction to save changes
    print("Customer data inserted successfully!")  # Success message
except mysql.connector.Error as err:
    print("Error:", err)           # Print error if insertion fails

cursor.close()  # Close cursor to free resources
conn.close()    # Close database connection
