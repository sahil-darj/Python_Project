import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# ---------- CONFIG ----------
matplotlib.rcParams['font.family'] = 'Segoe UI Emoji'  # Supports emojis on Windows
sns.set(style="whitegrid", palette="pastel")

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "customer_segmentation"
}
TABLE_NAME = "customers"

# ---------- LOAD DATA ----------
def load_data():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        query = f"SELECT * FROM {TABLE_NAME}"
        df = pd.read_sql(query, conn)
        conn.close()
        print("Original columns from DB:", df.columns.tolist())
        # Rename columns for easier plotting
        df.columns = ['ID', 'Name', 'Age', 'Income', 'SpendingScore', 'Frequency', 'Region', 'cluster']
        print("Renamed columns:", df.columns.tolist())
        return df
    except Exception as e:
        print("Database connection error:", e)
        return pd.DataFrame()

# ---------- VISUALIZE ----------
def visualize(df):
    if df.empty:
        print("No data to visualize.")
        return

    # 1. Scatterplot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="Income", y="SpendingScore", hue="Region", data=df, palette="coolwarm")
    plt.title("🛍️ Income vs Spending Score by Region")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Barplot
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Region", y="SpendingScore", data=df, estimator='mean', palette="mako")
    plt.title("📊 Average Spending Score by Region")
    plt.ylabel("Average Spending Score")
    plt.tight_layout()
    plt.show()

    # 3. Boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="Region", y="Income", data=df, palette="Set2")
    plt.title("💰 Income Distribution by Region")
    plt.tight_layout()
    plt.show()

    # 4. Cluster Scatterplot (if cluster column is present)
    if 'cluster' in df.columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x="Income", y="SpendingScore", hue="cluster", data=df, palette="tab10", style="cluster")
        plt.title("🎯 Clustering View: Income vs Spending Score")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# ---------- MAIN ----------
def main():
    df = load_data()
    visualize(df)

if __name__ == "__main__":
    main()
