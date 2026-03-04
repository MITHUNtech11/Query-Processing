import pandas as pd

# Sample sales_data DataFrame
sales_data = pd.DataFrame({
    'Item': ['Item1', 'Item2', 'Item1', 'Item3', 'Item2', 'Item1'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': [250, 450, 300, 200, 500, 350]
})

# Create Pivot Table with max and min sales
pivot_table = pd.pivot_table(
    sales_data,
    values='Sales',
    index='Item',
    aggfunc=['max', 'min']
)

print(pivot_table)