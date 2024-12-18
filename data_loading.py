import pandas as pd

def load_data(file_path):
    """
    Load dataset from a file path.
    :param file_path: Path to the dataset (CSV).
    :return: DataFrame containing the dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully: {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
