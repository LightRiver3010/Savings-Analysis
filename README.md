# Savings Simulator
A web app (currently in demo) that helps users better grasp their spending habits and discover actionable ways to save money. Built entirely off Python, using Streamlit for web deployment.

**[Try it Here](https://saving-sim.streamlit.app/)**

## About
This project started out with me asking: "How can I use my data analysis skills to make something *I would use?*
From there, we got this Savings Simulator—a tool that provides **actionable savings tips** rather than vague advice like "Cut down leisure spending" or "Use coupons when shopping."


Note: this is a **demo**, not a full app. Initially, I struggled to find a balance between actual usefulness and user data. After all, if someone knows enough about their spending to put all their info into a simulator, they probably don't need any advice.
In the end, I settled on **ficticious, AI-generated transaction data** for my analysis, with the idea being that, if partnered with a third-party app such as Plaid, the service would be fully personalized to a user's expenses.

The ficticious transaction data reflects **10 unique spending archetypes**. I figured that, by adding various archetypes, I was giving users more opportunities to relate, therefore increasing the likelihood of the app being useful.
In the demo, users can **act as one of these archetypes**, fully exploring their top expenses and spending habits through Monte Carlo visualizations, along with recieving customized tips depending on top spending categories.


## Major Features
- **10 Customer Archetypes —** Thrifty Thomas, Gas-guzzling Gus, and more, each with unique spending habits
- **Monte Carlo Simulation —** Runs thousands of scenarios based on monthly spending variations to predict future spending
- **Personalized Tips —** Curated suggestions based on an archetype's top 5 expense categories
- **Before/After Comparison —** Visualizes how heavily small changes can impact monthly spending distribution
- **Spending Breakdown —** Pie charts and category analysis to show where each archetype's money actually goes

## How It Works
1. **Choose an Archetype** — Pick the archetype that best reflects your spending habits
2. **Review Your Expenses** — See monthly averages, common purchases, and Monte Carlo predictions
3. **Select Savings Tips** — Check off on straight-forward, actionable changes you're willing to make
4. **See the Impact** — Compare predicted spending from before and after your changes

## Technical Aspects
**Data Analysis**
- **Pandas** for data manipulation, grouping, and aggregation across 10 customer profiles
- **NumPy** for running Monte Carlo simulations with normally distributed random sampling
- **Matplotlib** for displaying pie charts and Monte Carlo simulations

**Web App**
- **Streamlit** — Multi-page app with session state for saving user inputs
- **Dynamic Content** — Tips and stats generated based on archetype selection
- **Progress Indicators** — For easily comparing archetype spending habits

## Technologies Used
- Python 3
- Streamlit
- Pandas
- NumPy
- Matplotlib

## Data Files
- `fictitious_credit_card_transactions_final.xlsx` — Transaction data for 10 fictional archetypes
- `money_saving_tips_final.xlsx` — Savings tips, including estimated monthly impact
- `leisure_activities.csv` — Fun purchases to put potential savings into perspective
