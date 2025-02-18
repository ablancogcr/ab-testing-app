import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="A/B Test App",
    page_icon=":bar_chart:",
    layout="centered"
)

# Main title and introduction
st.title("Welcome to the A/B Testing App")
st.write('''
    An A/B test is at its core a simple way to compare two versions of something to figure out which performs better. 
    It is an application of statistical hypothesis testing with two variants leading to the technical terms A and B.
    
    ''')
st.markdown("**How does it work?**")
st.write(''' 
    The first step is to decide what it is you want to test. This could be anything from a marketing campaign to a new website design. 
    Then you need to decide what you want to measure. This could be anything from clicks to revenue. \n
    To run the test you randomly split your audience into two groups, A and B. Group A sees the original (control) and group B sees the new version (treatment).
    This can be for example, the color of a button, the text of a call to action, or the layout of the website. \n
    In real life, there can be many factors that can influence the behavior of users, this is why it is important to split audience as random as possible. \n
    Another key point is to have a large enough sample size to ensure the results are statistically significant. 
    There is a tradeoff between the confidence level and the sample size, the higher the confidence level the lower the risk of Type I error, but the larger the sample size needed. \n
    So, basically, when you choose a confidence level of 95%, you are saying that you are willing to accept a 5% chance to conclude that version B is better that A when there is actually no difference. \n
''')
st.markdown("**Some basic concepts**")
st.write('''
    - **Null Hypothesis (H0):** The null hypothesis states that there is no difference between the two groups.
    - **Alternative Hypothesis (H1):** The alternative hypothesis states that there is a difference between the two groups.
    - **p-value:** The probability that the observed difference (or a more extreme one) would occur if the null hypothesis is true.
    - **Confidence Level:** The probability that the confidence interval contains the true effect. For example, 95% means there is a 95% chance that the interval contains the true difference.
    - **Significance Level (α):** This is the threshold that determines if it is possible to reject H0. This happens when the p-value is less than α.
    - **Type I error (False Positive):** Expressed as a percentage, it is the probability of rejecting H0 when it is actually true.
    - **Type II error (False Negative):** Expressed as a percentage, it is the probability of failing to reject H0 when H1 is actually true.
''')
st.markdown("**Common mistakes**")
st.write('''
    - **Running the test for too short:** Sometimes you are in a hurry to get results. Due to the randomization it is important to let the test run for a reasonable amount of time. 
    - **Not having a large enough sample size:** This is related to the previous point. It is important to have a large enough sample size to ensure the results are statistically significant.
    - **Not having a clear hypothesis:** The test you are doing needs to be as clearly defined as possible.
''')
st.markdown("**Summary**")
st.write('''
    In short, A/B testing is a powerful tool to test changes in a controlled environment. It can be used in real life cases to test changes in a website, a marketing campaign, or a product; while at the same time providing statistical evidence to support the decision making process.
    But, it is also important to have a clear hypothesis, a large enough sample size, and to let the test run for a reasonable amount of time.
''')