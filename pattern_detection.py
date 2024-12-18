from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_clustering(df, features, n_clusters=3):
    """
    Perform KMeans clustering on the selected features.
    :param df: DataFrame containing the dataset.
    :param features: List of columns to use for clustering.
    :param n_clusters: Number of clusters to form.
    :return: DataFrame with cluster labels appended.
    """
    data = df[features]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(data)
    print(f"Clustering completed with {n_clusters} clusters.")
    return df

def plot_clusters(df, x_column, y_column, cluster_column, save_path=None):
    """
    Plot the clustering result.
    :param df: DataFrame with clustering results.
    :param x_column: Column for the x-axis.
    :param y_column: Column for the y-axis.
    :param cluster_column: Column containing cluster labels.
    :param save_path: Optional path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    for cluster in df[cluster_column].unique():
        cluster_data = df[df[cluster_column] == cluster]
        plt.scatter(cluster_data[x_column], cluster_data[y_column], label=f"Cluster {cluster}")
    plt.title(f"Clusters: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend()
    if save_path:
        plt.savefig(save_path)
    plt.show()
