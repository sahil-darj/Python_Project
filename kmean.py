import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load data from CSV file
def load_data():
    # Make sure 'cs.csv' file is in the same directory as this script
<<<<<<< HEAD
    df = pd.read_csv("customer_data.csv")
=======
    df = pd.read_csv("cs.csv")
>>>>>>> 91e291e1bad2f3e8455a1f28add62bea0b24712a
    return df

# Handle missing values in the dataset
def preprocess_data(df):
    # Fill missing values for correct columns
    for col in ['Annual_Income', 'Spending_Score']:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())
    return df

    return df

# Find optimal number of clusters using Elbow Method
def find_optimal_clusters(X):
    max_k = min(10, len(X))  # Avoid more clusters than samples
    if max_k < 2:
        print("Not enough samples to determine optimal clusters.")
        return
    
    distortions = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    sns.lineplot(x=range(1, max_k + 1), y=distortions, marker='o', linewidth=2.5)
    plt.title('Elbow Method to Determine Optimal Clusters')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia (WCSS)')
    plt.grid(True)
    plt.show()

# Apply KMeans clustering on features
def apply_kmeans(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)
    return kmeans, labels

# Plot clusters with centroids
def plot_clusters(df, kmeans):
    plt.figure(figsize=(10, 6))
    palette = sns.color_palette("bright", len(df['cluster'].unique()))
    sns.scatterplot(
    x='Annual_Income', y='Spending_Score', hue='cluster',
    data=df, palette=palette, s=100, edgecolor='black'
)

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=250, marker='X', label='Centroids')
    plt.title("Customer Segmentation", fontsize=16)
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    sns.set_context("talk")
    df = load_data()
    df = preprocess_data(df)

    X = df[['Annual_Income', 'Spending_Score']].values


    if len(X) < 2:
        print("Not enough data to perform clustering.")
        return

    if len(X) >= 4:
        find_optimal_clusters(X)

    n_clusters = min(5, len(X))
    kmeans, labels = apply_kmeans(X, n_clusters)
    df['cluster'] = labels

    plot_clusters(df, kmeans)

if __name__ == "__main__":
    main()
