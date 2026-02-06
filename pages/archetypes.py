import streamlit as st
from main import stats_relative

st.header("Choose your Achetype")

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
a.subheader("Standard Steve :man:")
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
if a.button("**Select Archetype**", key=counter):
    chosen_archetype = "Standard Steve"
counter += 1


b.subheader("Rideshare Ryan :red_car:")
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
if b.button("**Select Archetype**", key=counter):
    chosen_archetype = "Rideshare Ryan"
counter += 1


c.subheader("Shopping Sam :shopping_cart:")
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
if c.button("**Select Archetype**", key=counter):
    chosen_archetype = "Shopping Sam"
counter += 1


a.subheader("Moviegoer Mark :popcorn:")
a.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: High")
a.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: High")
a.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: High")
a.markdown(
    """
- Massive movie spender
- High phone bills
- Shops on Amazon frequently
"""
)
if a.button("**Select Archetype**", key=counter):
    chosen_archetype = "Moviegoer Mark"
counter += 1


b.subheader("Expensive Eli :moneybag:")
b.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: High")
b.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Very High")
b.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Very High")
b.markdown(
    """
- Huge gamer & Netflix fan
- Very high electric/water/phone bills
- Donates large amounts to charity
"""
)
if b.button("**Select Archetype**", key=counter):
    chosen_archetype = "Expensive Eli"
counter += 1


c.subheader("Gas-guzzling Gus :fuelpump:")
c.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: High")
c.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Very High")
c.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Very High")
c.markdown(
    """
- Spends tons on gas
- Moderate gamer & Spotify superfan
- Frequently shops online
"""
)
if c.button("**Select Archetype**", key=counter):
    chosen_archetype = "Gas-guzzling Gus"
counter += 1


a.subheader("Stylish Sabrina :high_heel:")
a.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Very High")
a.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Very High")
a.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: High")
a.markdown(
    """
- Spends lots at Old Navy
- Lots of monthly subscriptions
- High phone/cable bills
"""
)
if a.button("**Select Archetype**", key=counter):
    chosen_archetype = "Stylish Sabrina"
counter += 1


b.subheader("Amazon Andy :truck:")
b.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Very High")
b.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Medium")
b.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: High")
b.markdown(
    """
- Spends most earnings on Amazon
- High phone/cable bills
- Spends little on gas/movies/games
"""
)
if b.button("**Select Archetype**", key=counter):
    chosen_archetype = "Amazon Andy"
counter += 1


c.subheader("Gaming George :video_game:")
c.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Low")
c.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Medium")
c.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Medium")
c.markdown(
    """
- Frequently buys new games/consoles
- High electric/water bills
- Spends little on other categories
"""
)
if c.button("**Select Archetype**", key=counter):
    chosen_archetype = "Gaming George"
counter += 1


a.subheader("Thrifty Thomas :dollar:")
a.progress(((stats_relative.iloc[counter, 3]) / 4), text="Monthly Spending: Low")
a.progress(((stats_relative.iloc[counter, 4]) / 4), text="# Monthly Purchases: Low")
a.progress(((stats_relative.iloc[counter, 1]) / 4), text="Monthly Spending Variability: Low")
a.markdown(
    """
- Spends little on gas/food
- Enjoys shopping at Old Navy
- High cable/utility bills
"""
)
if a.button("**Select Archetype**", key=counter):
    chosen_archetype = "Thrifty Thomas"
counter += 1

if chosen_archetype != None:
    st.session_state.arch = chosen_archetype
    st.switch_page("pages/chosen_archetype.py")
    
    
    
