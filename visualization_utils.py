import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, save_path=None):
    """
    Plot a heatmap showing correlations between numerical features.
    :param df: DataFrame containing the dataset.
    :param save_path: Optional path to save the plot.
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_time_series(df, date_column, value_column, save_path=None):
    """
    Plot a time series for a given date and value column.
    :param df: DataFrame containing the dataset.
    :param date_column: Column with datetime information.
    :param value_column: Column with numerical values to plot.
    :param save_path: Optional path to save the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df[date_column], df[value_column], marker='o')
    plt.title(f"Time Series of {value_column}")
    plt.xlabel("Date")
    plt.ylabel(value_column)
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.show()
