# Zomato Data Analysis

# Step 1: Importing necessary Python libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Creating the data frame.
data_frame = pd.read_csv('Zomato-data-.csv')
print(data_frame.head())

# Step 3: Data Cleaning and Preparation

# 3. Convert the rate column to a float by removing denominator characters.
def handle_rate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

data_frame['rate'] = data_frame['rate'].apply(handle_rate)
print(data_frame.head())

# 4. Getting summary of the dataframe use df.info().
data_frame.info()

# 5. Checking for missing or null values to identify any data gaps.
print(data_frame.isnull().sum())

# Step 6: Exploring Restaurant Types
# 1. Let's see the listed_in (type) column to identify popular restaurant categories.
# sns.countplot(x=data_frame['listed_in(type)'])
# plt.xlabel("Type of restaurant")
# plt.show()


# 7. Votes by Restaurant Type

# grouped_data = data_frame.groupby('listed_in(type)')['votes'].sum()
# result = pd.DataFrame({'votes':grouped_data})
# plt.plot(result, c='green', marker='o')
# plt.xlabel("Type of restaurant")
# plt.ylabel("votes")
# plt.show()

# Step 8: Identify the Most Voted Restaurant
# Find the restaurant with the highest number of votes.

max_votes = data_frame['votes'].max()
restaurant_with_max_votes = data_frame.loc[data_frame['votes'] == max_votes, 'name'].tolist()

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)

# Step 9: Online Order Availability
# sns.countplot(x=data_frame['online_order'])
# plt.show()

# Step 10: Analyze Ratings
# Checking the distribution of ratings from the rate column.
# plt.hist(data_frame['rate'],bins=5)
# plt.title('Ratings Distribution')
# plt.show()

# Step 11: Approximate Cost for two people
# Analyze the approx_cost(for two people) column to find the preferred price range.
# couple_data=data_frame['approx_cost(for two people)']
# sns.countplot(x=couple_data)
# plt.show()

# Step 12: Ratings Comparison - Online vs Offline Orders
# Compare ratings between restaurants that accept online orders and those that don't.
# plt.figure(figsize = (6,6))
# sns.boxplot(x = 'online_order', y = 'rate', data = data_frame)
# plt.show()

# Step 13: Order Mode Preferences by Restaurant Type
pivot_table = data_frame.pivot_table(
    index='listed_in(type)', 
    columns='online_order', 
    aggfunc='size', 
    fill_value=0
)

sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Order Mode Preferences by Restaurant Type')
plt.xlabel('Online Order')
plt.ylabel('Restaurant Type')
plt.show()
