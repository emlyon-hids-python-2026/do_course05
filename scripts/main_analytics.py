# %% Import necessary libraries

import pandas as pd

# %% Load the dataset
df_sales_part1 = pd.read_csv('../data/Sales_MedicStore_part1.csv', sep=';')
df_sales_part2 = pd.read_csv('../data/Sales_MedicStore_part2.csv', sep=';')
df_mapping = pd.read_excel('../data/Mapping.xlsx')

# %% display the first few rows of the datasets

print("First few rows of Sales_MedicStore_part1.csv:")
print(df_sales_part1.head())

# %%

print("\nFirst few rows of Sales_MedicStore_part2.csv:")
print(df_sales_part2.head())

#%%

print("\nFirst few rows of Mapping.xlsx:")
print(df_mapping.head())

# %% Concatenate the two datasets
lst_sales = [df_sales_part1, df_sales_part2]
df_sales = pd.concat(lst_sales, ignore_index=True)

#%% Display the first few rows of the concatenated dataset

print("First few rows of the concatenated dataset:")
print(df_sales.head())
# %% Display the information of the datasets
print(df_sales.info())

# %% Display the information of the mapping dataset
print(df_mapping.info())

# %%  Merge the sales data with the mapping data
df_merged = pd.merge(df_sales, df_mapping, how='left', left_on='Sub-Category', right_on='Sub-Category')

# %% Display the first few rows of the merged dataset
print("First few rows of the merged dataset:")
print(df_merged.head())

# %% Calculate the Sales Amount for each row
df_merged['Sales Amount'] = df_merged['Quantity'] * df_merged['Unit Price']


# %% Answer to some business questions

# How many lines is there in the original tables (Sales_Part1, Sales_Part2 and mapping) ?
nb_lines_sales_part1 = len(df_sales_part1)
nb_lines_sales_part2 = len(df_sales_part2)
nb_lines_mapping = len(df_mapping)
print(f"\nNumber of lines in Sales_MedicStore_part1.csv: {nb_lines_sales_part1}")
print(f"Number of lines in Sales_MedicStore_part2.csv: {nb_lines_sales_part2}")
print(f"Number of lines in Mapping.xlsx: {nb_lines_mapping}")

# Make a general statistical description of the final table
df_statistics = df_merged.describe(include='all')
print("\nStatistics on the merged dataset:")
print(df_statistics)

# How many orders do we have ?
total_orders = df_merged['Order ID'].nunique()
print(f"\nTotal number of orders: {total_orders}")

# What is the total sales amount ?
total_sales_amount = df_merged['Sales Amount'].sum()
print(f"\nTotal Sales Amount: {total_sales_amount}")

# Who are the top 3 customers that makes the most purchases (order count)
df_top_customer = df_merged['Customer Name'].value_counts().head(3)
print(f"\nTop 3 customers who made the most purchases (order count):\n{df_top_customer}")

# What is the total Sales for France ?
total_sales_france = df_merged[df_merged['Country'] == 'France']['Sales Amount'].sum()
print(f"\nTotal Sales for France: {total_sales_france}")

# How much does the total Sales for France represent compare to the total global Sales
ratio_sales_france = total_sales_france / total_sales_amount
print(f"\nRatio of Sales Amount for France to Total Sales Amount: {ratio_sales_france*100:.2f}%")

#%% Create a disctionary to store the analysis results

dict_analysis = {
    "how many lines are in Sales_MedicStore_part1.csv": nb_lines_sales_part1,
    "how many lines are in Sales_MedicStore_part2.csv": nb_lines_sales_part2,
    "how many lines are in Mapping.xlsx": nb_lines_mapping,
    "how many orders do we have": total_orders,
    "what is the total sales amount": total_sales_amount,
    "What is the total Sales for France": total_sales_france,
    "How much does the total Sales for France represent compare to the total global Sales": ratio_sales_france
}

# Convert the dictionary to a DataFrame for better visualization
df_analysis = pd.DataFrame(list(dict_analysis.items()), columns=['Question', 'Answer'])

print("\nAnalysis Results:")
print(df_analysis)

# %% Save into Excel files

df_merged.to_excel('../data/merged_sales_data.xlsx')

df_analysis.to_excel('../data/analysis_results.xlsx')

df_statistics.to_excel('../data/statistics_results.xlsx')

df_top_customer.to_excel('../data/top_customers.xlsx')
# %%
