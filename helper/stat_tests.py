from scipy.stats import ttest_ind

def perform_ab_test(group_A, group_B, confidence_level=0.95, hypothesis_type="Two Tails"):
    """
    Perform a t-test between two groups with options for one-tailed or two-tailed hypotheses.
    
    Parameters:
        group_A (array-like): Outcome data for group A.
        group_B (array-like): Outcome data for group B.
        confidence_level (float): Confidence level (e.g., 0.95 for 95%).
        hypothesis_type (str): "One Tail" or "Two Tails".
    
    Returns:
        tuple: (t_stat, p_val, decision) where:
            - t_stat: t-statistic
            - p_val: p-value (adjusted if one-tailed)
            - decision: interpretation message regarding statistical significance.
    """
    # Perform a two-sample t-test (returns two-tailed p-value by default)
    t_stat, p_val = ttest_ind(group_A, group_B, equal_var=False)
    
    # Adjust p-value if testing a one-tailed hypothesis
    if hypothesis_type.lower() == "one tail":
        p_val /= 2
    
    alpha = 1 - confidence_level
    if p_val < alpha:
        decision = True
    else:
        decision = False
    
    return t_stat, p_val, decision
