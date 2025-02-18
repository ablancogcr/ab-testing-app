import numpy as np
import pandas as pd

def generate_synthetic_ab_data(sample_size: int) -> pd.DataFrame:
    """
    Generate a synthetic A/B testing dataset using NumPy.
    
    Parameters:
        sample_size (int): Number of rows to generate per group.
    
    Returns:
        pd.DataFrame: A DataFrame with columns 'group' and 'outcome'
                      containing synthetic data for groups A and B.
    """
    # Set a seed for reproducibility
    #np.random.seed(42)
    
    # Generate synthetic outcomes for group A and group B
    outcomes_A = np.random.normal(loc=50, scale=10, size=sample_size)
    outcomes_B = np.random.normal(loc=55, scale=10, size=sample_size)
    
    # Create DataFrames for each group
    df_A = pd.DataFrame({'group': 'A', 'outcome': outcomes_A})
    df_B = pd.DataFrame({'group': 'B', 'outcome': outcomes_B})
    
    # Combine the DataFrames into a single one
    return pd.concat([df_A, df_B], ignore_index=True)
