def clean_data(df):
    """
    Clean the dataset by removing rows with missing values.
    :param df: DataFrame to clean.
    :return: Cleaned DataFrame.
    """
    print(f"Original dataset shape: {df.shape}")
    cleaned_df = df.dropna()
    print(f"Cleaned dataset shape: {cleaned_df.shape}")
    return cleaned_df
