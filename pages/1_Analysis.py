import streamlit as st
import pandas as pd
import numpy as np
import os

import seaborn as sns
import matplotlib.pyplot as plt

from helper.data_generation import generate_synthetic_ab_data
from helper.stat_tests import perform_ab_test

st.title('A/B Test Data Analysis')

# Initialize session state for data persistence
if 'df' not in st.session_state:
    st.session_state.df = None

# ------------------------------
# Step 1: Load Your Data
# ------------------------------
st.subheader('Step 1: Load Your Data')
st.write(
    '''
    Upload your CSV file containing A/B test data, or use the sample dataset provided below. 
    Please take into account that the file you upload must contain a column named 'group' with values 'A' and 'B' and the corresponding data to be evaluated.
    This data can be visit, clicks, conversion rates or any other metric you want to compare between the two groups.
    '''
)

# Option 1: File Upload
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

st.write('Below you can download a sample CSV file that shows the way the data should be structured. There should be two columns: the first one for the group, either A or B, and a second column with the outcomes.')
sample_file_path = os.path.join("sample", "ab_sample.csv")

with open(sample_file_path, "rb") as file:
    st.download_button(
        label="Download Sample File",
        data=file,
        file_name="sample_file.csv",
        mime="text/csv"
    )


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df
    st.success("Data loaded successfully!")
else:
    st.write("Or generate a sample dataset using the form below:")
    with st.form(key="sample_data_form"):
        sample_size = st.number_input(
            "Enter sample size per group:",
            min_value=100,
            value=1000,
            step=10
        )
        submit_button = st.form_submit_button("Generate Sample Data")
    
    if submit_button:
        df = generate_synthetic_ab_data(int(sample_size))
        st.session_state.df = df
        st.success("Sample dataset generated! Note: This data is created using a Normal Distribution.")
    else:
        df = None

# ------------------------------
# Step 2: Review Your Data
# ------------------------------
if st.session_state.df is not None:
    st.divider()
    df = st.session_state.df
    
    st.subheader('Step 2: Review Your Data')
    st.write('''
        Now that we have some data, let's review the summary statistics for each group. 
        In the table below you can see the mean, standard deviation, minimum, maximum and other statistics for each group. The data at 50% is the median.  ''')

    st.write("**Groups Summary Statistics**")
    summary_A = df[df["group"] == "A"]["outcome"].describe()
    summary_B = df[df["group"] == "B"]["outcome"].describe()
    summary_table = pd.DataFrame({
        "Group A": summary_A,
        "Group B": summary_B
    })
    st.dataframe(summary_table)

    # Calculate means for plotting
    mean_A = df[df["group"] == "A"]["outcome"].mean()
    mean_B = df[df["group"] == "B"]["outcome"].mean()

    st.subheader("Outcome Distribution with Density and Mean Lines")
    plt.figure(figsize=(10, 6))
    
    # Plot density-normalized histograms for both groups using Seaborn
    sns.histplot(
        data=df,
        x="outcome",
        hue="group",
        bins=30,
        stat="density",  # Normalize to density
        alpha=0.5,
        element="step",
        kde=False  # We'll add KDE separately for more control
    )
    
    # Overlay KDE plots for smoother density curves
    sns.kdeplot(data=df, x="outcome", hue="group", common_norm=False, linewidth=2)
    
    # Add vertical dashed lines for the mean of each group
    plt.axvline(mean_A, color="blue", linestyle="--", linewidth=2, label=f"Mean A: {mean_A:.2f}")
    plt.axvline(mean_B, color="red", linestyle="--", linewidth=2, label=f"Mean B: {mean_B:.2f}")
    
    plt.title("Outcome Distribution by Group")
    plt.xlabel("Outcome")
    plt.ylabel("Density")
    plt.legend()
    
    st.pyplot(plt.gcf())
    
    # ------------------------------
    # Step 3: Perform A/B Test
    # ------------------------------
    st.divider()
    st.subheader("Step 3: Perform A/B Test")
    with st.form(key="ab_test_form"):
        # Row 1: Confidence Level selection and explanation
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            confidence_option = st.selectbox(
                "Select Confidence Level:",
                options=["90%", "95%", "99%"],
                index=1  # Default to 95%
            )
        with row1_col2:
            st.write("The confidence level is the probability that the confidence interval contains the true effect. For example, 95% means there is a 95% chance that the interval contains the true difference.")
        
        # Row 2: Hypothesis Type selection and explanation
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            hypothesis_option = st.selectbox(
                "Select Hypothesis Type:",
                options=["One Tail", "Two Tails"],
                index=1  # Default to Two Tails
            )
        with row2_col2:
            st.write("One-tailed tests check for an effect in a specific direction, whereas two-tailed tests check for any difference regardless of direction.")
        
        # Row 3: Submit Button (placed in the first column)
        row3_col1, row3_col2 = st.columns(2)
        with row3_col1:
            test_submit = st.form_submit_button("Run A/B Test")
        with row3_col2:
            st.write('''
                Running the test will perform the following Hipothesis Test:
                \n H0: The difference between the groups is not statistically significant. 
                \n H1: The difference between the groups is statistically significant.
            ''')
    
    if test_submit:
        # Convert the confidence level string (e.g., "95%") to a float (0.95)
        confidence_level = float(confidence_option.strip("%")) / 100
        
        # Get outcome data for each group
        group_A_vals = df[df["group"] == "A"]["outcome"]
        group_B_vals = df[df["group"] == "B"]["outcome"]
        
        # Call the helper function to perform the A/B test
        t_stat, p_val, decision = perform_ab_test(
            group_A_vals,
            group_B_vals,
            confidence_level=confidence_level,
            hypothesis_type=hypothesis_option
        )
        
        st.write("**A/B Test Results**")

        if decision == True:
            st.success(f"Given the data available: P-value {p_val:.4f} is less than {1-confidence_level:.2f} (Confidence level). We can reject H0 and say that with the data provided the difference between groups is statistically significant and that this difference is not caused by chance.")
        else:
            st.warning(f"Given the data available: P-value {p_val:.4f} is greater than {1-confidence_level:.2f} (Confidence level). We can not reject H0 and say that the difference between groups is not statistically significant.")

        st.write(f"T-Statistic: {t_stat:.4f}")
        st.write(f"P-Value: {p_val:.4f}")
        st.write(f"Confidence Level: {1-confidence_level:.4f}")
        st.write('''
                What just happened here is that a Welch's t-test was performed to compare the means of the two groups. 
                This test has the assumption that we don't know the population standard deviation and that the samples have different variances. 
                This is an useful assumption to use in real life scenarios where we don't have access to the population data and is commonly used in A/B testing.
            ''')
        st.write('''
                It is also important to note that Confidence Level is also known as Alpha, and it is the probability of rejecting the null hypothesis when it is true. This is also called Type I error.
        ''')

