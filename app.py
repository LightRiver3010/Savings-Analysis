import streamlit as st

st.title("Savings Simulator Demo :money_with_wings:")
st.subheader("Welcome to my Savings Demo!")
st.write("In this demo, you will:")
st.markdown("1. Algin yourself with a customer archetype that **best matches your spending patterns** :white_check_mark: \n 2. Proceed through the savings sim as that customer, seeing current expenses & areas for savings :white_check_mark: \n3. **Learn tips for saving money** based on your customer's highest expenses :white_check_mark: \n4. **See how much those tips can save you** each month :white_check_mark: ")
st.markdown("If that sounds good to you, then :point_down:*press the button below to begin!* :point_down:")
if st.button("Begin"):
    st.switch_page("pages/archetypes.py")
    
st.write("(or, if you'd like to hear about why I made this project, click below)")
if st.button("About"):
    st.switch_page("pages/why.py")