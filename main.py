import os
from utils.data_loading import load_data
from utils.data_cleaning import clean_data
from utils.visualization_utils import plot_correlation_matrix, plot_time_series
from analysis.pattern_detection import perform_clustering, plot_clusters

def main():
    # File paths
    raw_data_path = "data/raw/dataset.csv"
    cleaned_data_path = "data/processed/cleaned_dataset.csv"
    
    # Load data
    df = load_data(raw_data_path)
    if df is None:
        return
    
    # Clean data
    cleaned_df = clean_data(df)
    cleaned_df.to_csv(cleaned_data_path, index=False)
    
    # Visualizations
    plot_correlation_matrix(cleaned_df, save_path="output/correlation_matrix.png")
    
    # Time series analysis (if applicable)
    if 'Date' in cleaned_df.columns and 'Value' in cleaned_df.columns:
        cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'])
        plot_time_series(cleaned_df, date_column='Date', value_column='Value', save_path="output/time_series.png")
    
    # Clustering example
    if {'Feature1', 'Feature2'}.issubset(cleaned_df.columns):
        clustered_df = perform_clustering(cleaned_df, features=['Feature1', 'Feature2'], n_clusters=3)
        plot_clusters(clustered_df, x_column='Feature1', y_column='Feature2', cluster_column='Cluster', save_path="output/clusters.png")

if __name__ == "__main__":
    main()
