import numpy as np
import pandas as pd


# CHANGE THE NAMES OF THE COLUMNS TO LOWER CASE AND REMOVE WHITE SPACES
def change_col_names_to_lower_case(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function changes the case of the column names to lowercase.

    Args:
    - df (DataFrame): The input DataFrame.

    Returns:
    - DataFrame: A new DataFrame with lowercase column names.
    '''
    # Create a new DataFrame with lowercase column names
    #df1 = df.copy()
    df.columns = df.columns.str.lower()
    
    return df
#CHECKING UNIQUE VALUES IN ALL COLUMNS
def unique_value(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function caculates the uniques vales for all the columns

    Args:
    - df (DataFrame): The input DataFrame.

    Returns:
    - DataFrame: A new DataFrame with lowercase column names.
    '''
    # Create a new DataFrame with lowercase column names
    
    for col in df.columns:
        unique_val = df[col].unique()
        print("Unique values for" , col, "is" ,unique_val)

