import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from main import generate_monte_carlo, avg_monthly_expense_total


monthly_saved = st.session_state.monthly_saved
before_fig = st.session_state.before_fig
before_ax = st.session_state.before_ax
chosen_archetype = st.session_state.arch
before_finals = st.session_state.before_finals
before_finals_df = st.session_state.before_finals_df
before_top_10 = st.session_state.before_top_10
before_low_10 = st.session_state.before_top_10


st.header("Your Savings")
st.write(f"Overall, by making a few relatively small changes, you saved an average of ${monthly_saved} per month!")
st.write(f"Let's see how this compares to your previous spending habits.")
st.subheader("Before vs. After")
st.write("Below, in red, is your 'before' simulation, showing how much you were likely to spend each month before the savings. The green is the 'after,' showing how much you're likely to spend after making these simple changes.")


after_fig, after_ax, finals, months = generate_monte_carlo(chosen_archetype, monthly_saved, "green")
before_ax.hist(finals, bins=150, color="green", alpha=0.75)
st.pyplot(before_fig)

finals_df = pd.DataFrame(finals)
finals_df.columns = ['price']
after_top_10 = finals_df['price'].quantile(0.90).round(2)
after_low_10 = finals_df['price'].quantile(0.10).round(2)

avg_before = avg_monthly_expense_total(chosen_archetype)
avg_after = avg_monthly_expense_total(chosen_archetype, monthly_saved)
avg_diff = avg_before - avg_after

st.markdown(f"Whereas before your worst case scenario was spending \${before_top_10}, now it's only spending \${after_top_10}. That's a \${(before_top_10 - after_top_10).round(2)} difference each month!")
st.markdown(f"**Average monthly spending before:** ${avg_before}")
st.markdown(f"**Average monthly spending after:** ${avg_after}")
st.markdown(f"**Average Monthly difference in spending:** ${avg_diff}")

st.write("Done reviewing your graphs? If so, let's proceed to a summary of what we've learned.")
if st.button("Continue"):
    st.session_state.avg_diff = avg_diff
    st.session_state.after_fig = before_fig
    st.switch_page("pages/summary.py")