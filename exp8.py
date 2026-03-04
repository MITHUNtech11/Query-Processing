import pandas as pd

# Sample sales_data DataFrame
sales_data = pd.DataFrame({
    'Item': ['Item1', 'Item2', 'Item1', 'Item3', 'Item2', 'Item1'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Units_Sold': [10, 15, 20, 12, 18, 25]
})

# Create Pivot Table to find item-wise total units sold
pivot_table = pd.pivot_table(
    sales_data,
    values='Units_Sold',
    index='Item',
    aggfunc='sum'
)

print(pivot_table)