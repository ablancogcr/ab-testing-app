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
    # Calculate the mean for each group
    scale = np.random.randint(1,5)
    #print(f"scale: {scale}")

    loc_A = np.random.normal(loc=50, scale=scale, size=1)
    loc_B = np.random.normal(loc=50, scale=scale, size=1)
    
    # Generate synthetic outcomes for group A and group B
    scale_A = np.random.randint(5,10)
    scale_B = np.random.randint(5,10)
    outcomes_A = np.random.normal(loc=loc_A, scale=scale_A, size=sample_size)
    outcomes_B = np.random.normal(loc=loc_B, scale=scale_B, size=sample_size)
    
    # Create DataFrames for each group
    df_A = pd.DataFrame({'group': 'A', 'outcome': outcomes_A})
    df_B = pd.DataFrame({'group': 'B', 'outcome': outcomes_B})
    
    # Combine the DataFrames into a single one
    return pd.concat([df_A, df_B], ignore_index=True)
