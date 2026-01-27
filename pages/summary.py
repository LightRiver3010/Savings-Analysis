import streamlit as st
import pandas as pd
import numpy as np
import math

tips_used = st.session_state.tips_used
avg_diff = st.session_state.avg_diff

st.header("Summary")

st.subheader("The Savings")
st.write("Below are the savings tips you chose:")
for i in tips_used:
    st.markdown(
        f"""
    - {i}
        """
    )

st.markdown(f"...and, by adapting these simple changes, you could save up to **${avg_diff} each month.**")

st.subheader("New Spending")
st.write("But what can you do with all this saved money? Let's put it into perspective...")

leisure_df = pd.read_csv('data/leisure_activities.csv')
leisure_df = leisure_df[leisure_df['category'] != 'small']
leisure_df = leisure_df[leisure_df['category'] != 'small-medium']

for i in leisure_df['category'].unique():
    temp_df = leisure_df[leisure_df['category'] == i]
    for j in range(2):
        random_index = np.random.randint(0, len(temp_df)-1)
        random_purchase_row = temp_df.iloc[random_index]
        random_cost = random_purchase_row[1]
        random_purchase = random_purchase_row[0]
        n_months = math.ceil(random_cost / avg_diff)
        st.markdown(f"After **{n_months}** month(s): **{random_purchase} (\${random_cost}).**")

st.subheader("The Lesson")
st.markdown("""
    As you can hopefully see, small changes in your spending habits can add up to a big difference.
    It's as Benjamin Franklin once said:
    
    *"Watch the pennies and the dollars will take care of themselves."*
    
    These tips are about more than saving up for a new vacation or activity, though.
    They're about living a lifestyle where money is spent on purchases that are truly important, not the newest craze or interesting thing. 
    After all, if you make the decision to put away more than you spend, you'll start saving money no matter what your financial situation!
    
    So, now all that's left is for you to go take action. **Get out there and save some money!**
            """)

st.subheader("Thanks!")
st.markdown("""
    If you've gotten this far into the simulation, I want to say thank you for testing the Demo!
    My goal with this project was to make a product genuinely useful, and I truly hope this was fulfilled by helping you learn something about spending money.
    
    If you have any feedback on this demo, feel free to anytime [email me](mailto:james.savaryn@gmail.com).
    
    If you'd like to test out any of my other projects, check out [my website](https://savaryn.me/).
    
    If you want to see any of the code for this project (written fully in Python, using Pandas, numPy, Streamlit, and Matplotlib), check out the GitHub repository [here](https://www.github.com).
    
    Or, if you'd like to restart the demo and play as another archetype, click the button below!
            """)

if st.button("Restart"):
    st.switch_page("app.py")
