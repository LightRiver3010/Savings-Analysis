import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('data/fictitious_credit_card_transactions_final.xlsx')

df['large_purchase'] = df['price'] > 75
df['date_of_purchase'] = pd.to_datetime(df['date_of_purchase'])
df['week_number'] = df['date_of_purchase'].dt.strftime('%U')
df['month_number'] = df['date_of_purchase'].dt.strftime('%m')
df[['week_number', 'month_number', 'customer_id']] = df[['week_number', 'month_number', 'customer_id']].astype({'week_number' : int, 'month_number' : int, 'customer_id' : 'string'})
df[['customer_id', 'item_name', 'item_genre', 'location_of_purchase']] = df[['customer_id', 'item_name', 'item_genre', 'location_of_purchase']].astype({'customer_id' : 'string', 'item_name' : 'string', 'item_genre' : 'string', 'location_of_purchase' : 'string'})

mapp = {
    'C001' : 'Standard Steve',
    'C002' : 'Rideshare Ryan',
    'C003' : 'Shopping Sam',
    'C004' : 'Moviegoer Mark',
    'C005' : 'Expensive Eli',
    'C006' : 'Gas-guzzling Gus',
    'C007' : 'Stylish Sabrina',
    'C008' : 'Amazon Andy',
    'C009' : 'Gaming George',
    'C010' : 'Thrifty Thomas'
}
df['customer_id'] = df['customer_id'].map(mapp)

tips = pd.read_csv('data/Expense Savings Tips (All).csv')
mapping = {
    'FOOD_RETAIL_GROCERIES' : 'Food',
    'DINING' : 'Food',
    'TRANSPORTATION' : 'Transport',
    'TRAVEL_FLIGHTS' : 'Leisure',
    'TRAVEL_LODGING' : 'Leisure',
    'GENERAL_MERCHANDISE' : 'Retail',
    'RENT_AND_UTILITIES' : 'Bill'
}
tips['Category'] = tips['Category'].replace(mapping)

def get_tips(tips, customer_id):
    categories = find_top_item_genres(customer_id)[:5]
    suggestions = tips[tips['Category'].isin(categories)]
    user_tips = []
    for i in categories:
        for j in range(3):
            category_tips = suggestions[suggestions['Category'] == i]['Tip']
            category_savings = suggestions[suggestions['Category'] == i]['Est. Monthly Savings']
            random_tip = np.random.randint(0, 10)
            suggest = category_tips.iloc[random_tip]
            saving = category_savings.iloc[random_tip]
            while (suggest, saving) in user_tips:
                random_tip = np.random.randint(0, 10)
                suggest = category_tips.iloc[random_tip]
                saving = category_savings.iloc[random_tip]
            user_tips.append((suggest, saving))
    return user_tips

def generate_monte_carlo(user_id, diff = 0, color="red"):
    # months = int(input("How many months in advance would you like the simulation to run?"))
    sim_num = 10000
    months = 3
    finals = []
    testing = df[df['customer_id'] == user_id]
    testing = testing.groupby(['customer_id', 'month_number'])['price'].sum().reset_index()
    c_mean = testing['price'].mean()
    c_std = testing['price'].std()
    for i in range(sim_num):
        month_spending = np.random.normal(c_mean - diff, c_std, months).round(2)
        finals.append(month_spending.sum())
    finals = np.array(finals)
    fig, ax = plt.subplots(figsize=(7,4))
    ax.hist(finals, bins=150, color=color, alpha=0.75)
    ax.set_ylabel("# of Occurrences")
    ax.set_xlabel(f"Total estimated spending over next {months} months")
    return fig, ax, finals, months
    
    
def show_values(pct, data):
    absolute = int((pct / 100) * np.sum(data))
    return f'${absolute}'

def generate_expense_pie_chart(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby('item_genre')['price'].sum().reset_index()
    customer_df.set_index('item_genre', inplace=True)
    fig, ax = plt.subplots(figsize=(7, 7))
    customer_df.plot.pie(y='price', ax=ax, figsize=(10,10), autopct= lambda x: show_values(x, customer_df['price']))
    return fig


def avg_spending_std_monthly(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['customer_id', 'month_number'])['price'].sum().reset_index()
    customer_std = (customer_df['price'].std()).round(2)
    return customer_std

def avg_spending_std_weekly(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['customer_id', 'week_number'])['price'].sum().reset_index()
    customer_std = (customer_df['price'].std()).round(2)
    return customer_std

def avg_monthly_expense_total(customer_id, diff = 0):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['month_number'])['price'].sum().reset_index()
    n = customer_df['month_number'].nunique()
    avg_monthly_expenses = ((customer_df['price'].sum() - (n * diff)) / n).round(2)
    return avg_monthly_expenses

def avg_monthly_expenses_count(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['month_number'])['price'].count().reset_index()
    avg_monthly_expenses = ((customer_df['price'].sum()) / customer_df['month_number'].nunique()).round()
    return avg_monthly_expenses

def most_common_expenses_per_category(customer_id):
    top = {}
    customer_df = df[df['customer_id'] == customer_id]
    sorted_expenses = customer_df.groupby(['item_genre', 'location_of_purchase'])['price'].count().reset_index()
    sorted_expenses = sorted_expenses.sort_values(by=['item_genre', 'price'], ascending=False)
    for i in sorted_expenses['item_genre'].unique():
        top[f'{i}'] = (sorted_expenses[sorted_expenses['item_genre'] == i]['price'].max()), sorted_expenses[sorted_expenses['item_genre'] == i]['location_of_purchase'].iloc[:3]
    return top

def top_categories(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['item_genre'])['price'].sum().reset_index()
    customer_df = customer_df.sort_values(by=['price'], ascending=False)[:5]['item_genre'].tolist()
    return customer_df

def top_expense_per_category(customer_id):
    top = {}
    customer_df = df[df['customer_id'] == customer_id]
    sorted_expenses = customer_df.groupby(['item_genre', 'location_of_purchase'])['price'].sum().reset_index()
    sorted_expenses = sorted_expenses.sort_values(by=['item_genre', 'price'], ascending=False)
    for i in sorted_expenses['item_genre'].unique():
        top[f'{i}'] = (sorted_expenses[sorted_expenses['item_genre'] == i]['price'].max()).round(2), sorted_expenses[sorted_expenses['item_genre'] == i]['location_of_purchase'].iloc[:3]
    return top

def find_top_item_genres(customer_id):
    customer_df = df[df['customer_id'] == customer_id]
    customer_df = customer_df.groupby(['item_genre'])['price'].sum().reset_index().sort_values(by=['price'], ascending=False)['item_genre'].tolist()
    return customer_df

master_dict = {}
for i in df['customer_id'].unique():
    master_dict[i] = {
        'Average Monthly Spending STD' : avg_spending_std_monthly(i),
        'Average Weekly Spending STD' : avg_spending_std_weekly(i),
        'Average Monthly Expense Total' : avg_monthly_expense_total(i),
        'Average Monthly Expense Count' : avg_monthly_expenses_count(i),
        'Top Item Genres' : find_top_item_genres(i),
        'Top Expense per Category' : top_expense_per_category(i),
        'Moast Common Expenses per Category' : most_common_expenses_per_category(i)
    }
    
master_df = pd.DataFrame.from_dict(master_dict, orient='index')
master_df = master_df.reset_index(names='customer_id')
# print(master_df)

def gather_stats_relative():
    stats_dict = {}
    for z in master_df.columns[1:5]:
        avgg = master_df[z].mean()
        stdd = master_df[z].std()
        std_high = avgg + stdd
        std_low = avgg - stdd
        count = 0
        stats_dict[z] = {}
        for i in master_df['customer_id']:
            j = master_df.iloc[count].loc[z]
            if j > avgg:
                if j >= std_high:
                    stats_dict[z][i] = 4
                else:
                    stats_dict[z][i] = 3
            else:
                if j <= std_low:
                    stats_dict[z][i] = 1
                else:
                    stats_dict[z][i] = 2
            count += 1
    return stats_dict

stats_relative = gather_stats_relative()
stats_relative = pd.DataFrame.from_dict(stats_relative)
stats_relative = stats_relative.reset_index()