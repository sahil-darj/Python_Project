# Customer Segmentation using K-Means Clustering

This project performs **customer segmentation** using the **K-Means clustering** algorithm.  
It processes customer data, stores it in a MySQL database, and generates visualizations for better insights.

---

## 📂 Project Structure

- **clustered_customers.csv** – Output file containing clustered customer data.  
- **customer_data.csv** – Input dataset of customer details.  
- **create_table.py** – Script to create the required MySQL table.  
- **database.py** – Handles database connection.  
- **insert_data.py** – Inserts processed data into the database.  
- **manual_insert1.py** – Manually inserts sample data into the database.  
- **kmean.py** – Main script to run K-Means clustering on customer data.  
- **visualize.py** – Generates graphs and visualizations of clusters.  
- **requirements.txt** – Python dependencies for the project.  
- **customer_segmentation k-mean.pptx** – Project presentation file.

---

## 🛠 Requirements

Install dependencies using:
```
pip install -r requirements.txt
```

🗄 Database Setup

1:-- Install MySQL and create a database (e.g., customer_segmentation).

2:-- Update database.py with your MySQL username and password.

3:-- Run:

```
python create_table.py
```

4:-- Insert data:
```
python insert_data.py

```


🚀 How to Run

1:-- Run K-Means clustering:
```
python kmean.py
```
2:-- View results in:

clustered_customers.csv

Database table (if configured)

3:-- Generate visualization:

```
python visualize.py
```
📊 Output Example

Clustered data with labels

Scatter plots showing customer segments

Saved CSV with cluster IDs

💡 Use Case

This project can help:

Marketing teams identify customer groups

Businesses target specific customer segments

Analysts explore buying patterns
