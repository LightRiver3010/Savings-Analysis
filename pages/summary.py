import streamlit as st
import pandas as pd
import numpy as np
import math
from main import download

tips_used = st.session_state.tips_used
avg_diff = st.session_state.avg_diff
after_fig = st.session_state.after_fig

st.header("Summary :bookmark_tabs:")

st.subheader("The Savings :100:")
st.write("Below are the **savings tips you chose:**")
for i in tips_used:
    st.markdown(
        f"""
    - {i}
        """
    )

st.markdown(f"...and, by adapting these simple changes, you could save up to **${avg_diff} each month.**")

st.subheader("New Spending :gem:")
st.write("*But what can you do with all this saved money?* Let's put it into perspective...")

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

st.subheader("The Lesson :trophy:")
st.markdown("""
    As you can hopefully see, *small changes* in your spending habits can add up to a **big difference.**
    It's as Benjamin Franklin once said:
    
    *"Watch the pennies and the dollars will take care of themselves..."* :chart_with_upwards_trend:
    
    These tips are about more than saving up for a new vacation or activity, though.
    They're about living a lifestyle where **money is spent on purchases that are truly important,** not the newest craze or interesting thing. 
    After all, if you make the decision to put away more than you spend, **you'll start saving money no matter what your financial situation!**
    
    So now, all that's left is for you to go take action. **Get out there and save some money!**
            """)

#Report goes Here
report = download(avg_diff, tips_used, after_fig)
st.download_button(
    label="**Download Savings Report**",
    data=report,
    file_name="SavingsReport.png",
    mime="image/png"
)

st.subheader("Thanks! :heart:")
st.markdown("""
    If you've gotten this far into the simulation, I want to say **thank you for testing the Demo!**
    My goal with this project was to make a product genuinely useful, and I truly hope this was fulfilled by helping you learn something about spending money. :euro:
    
    If you have any *feedback* on this demo, feel free to **[email me](mailto:james.savaryn@gmail.com)**. :postbox:
    
    If you'd like to test out any of my *other projects,* check out **[my website](https://savaryn.me/)**. :computer:
    
    If I make an *update* to this web app, it'll likely be on my **[LinkedIn profile](https://www.linkedin.com/in/jsavaryn/)**. :link:
    
    If you want to see any of the *code for this project* (written fully in Python, using Pandas, numPy, Streamlit, and Matplotlib), check out the **[GitHub Repository](https://github.com/LightRiver3010/Savings-Analysis)**. :floppy_disk:
    
    Or, if you'd like to *restart the demo* and play as another archetype, **click the button below!**
            """)

if st.button(":rewind: **Restart**"):
    st.switch_page("app.py")
