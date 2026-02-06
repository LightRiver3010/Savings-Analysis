import streamlit as st
import pandas as pd
from main import get_tips, top_categories

tips = pd.read_excel('data/money_saving_tips_final.xlsx')
chosen_archetype = st.session_state.arch


st.header("Customized Savings Tips :moneybag:")
st.write("See below for some savings tips chosen *specifically for your top spending categories*. Feel free to **check off any of the tips** that you feel able to take action on!")

if 'user_tips' not in st.session_state:
    user_tips = get_tips(tips, chosen_archetype)
    st.session_state.user_tips = user_tips

top_user_categories = top_categories(chosen_archetype)

count = 0
for i in top_user_categories:
    st.subheader(f"{i}")
    for j in range(3):
        st.checkbox(f"{st.session_state.user_tips[count][0]}", key=count)
        count += 1
    
monthly_saved = 0
tips_used = []
for i in range(len(st.session_state.user_tips)):
    if st.session_state[i]:
        monthly_saved += int(st.session_state.user_tips[i][1])
        tips_used.append(st.session_state.user_tips[i][0])


st.write("Done saving? :white_check_mark: Let's proceed to the final stage to **see how much your monthly bill has changed.**")
if st.button("**Continue**"):
    st.session_state.tips_used = tips_used
    if monthly_saved < 1:
        monthly_saved = 1
    st.session_state.monthly_saved = monthly_saved
    st.switch_page("pages/carlo_after.py")