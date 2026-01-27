import streamlit as st
from main import stats_relative

st.header("Choose your Achetype")
st.write("Choose the character archetype below that most closely aligns with your current spending habits.")

chosen_archetype = None

# All the info for these archetypes is coming from my main.ipynb file, where I 
# did all the data analysis. I'm choosing to copy it over manually rather than import
# it an select all I need, as it is easier to do so. I'm not lazy, just working smarter!

data = {
    'Name' : ['Standard Steve', 'Rideshare Ryan', 'Shopping Sam'],
    'Average Monthly Expenses' : [1993.34, 2269.50, 2127.60],
    'Average Monthly Expense Count' : [36, 38, 37],
    'Top Genre' : ['Transport', 'Other', 'Transport']
}

a, b, c = st.columns(3)
counter = 0
a.subheader("Standard Steve")
a.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Average")
a.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Average")
a.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Low")
a.markdown(
    """
- Big gas spender
- Spotify & Netflix Subscriptions
- Regular moviegoer
"""
)
if a.button("Select Archetype", key='1'):
    chosen_archetype = "Standard Steve"
counter += 1


b.subheader("Rideshare Ryan")
b.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: High")
b.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: High")
b.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Average")
b.markdown(
    """
- Uses Uber/Lyft Often
- Shops a lot on Amazon
- High electric/water bills
"""
)
if b.button("Select Archetype", key='2'):
    chosen_archetype = "Rideshare Ryan"
counter += 1


c.subheader("Shopping Sam")
c.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Average")
c.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Average")
c.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Average")
c.markdown(
    """
- Spends a ton grocery shopping
- Few leisure purchases/large bills
- Moderate-high gas spending
"""
)
if c.button("Select Archetype", key='3'):
    chosen_archetype = "Shopping Sam"
counter += 1

# a.subheader("Moviegoing Mark")

if chosen_archetype != None:
    st.session_state.arch = chosen_archetype
    st.switch_page("pages/chosen_archetype.py")
    
    
    
