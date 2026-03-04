import pandas as pd

# Read the CSV file
df = pd.read_csv("employees.csv")

# Select distinct department IDs
distinct_departments = df['DEPARTMENT_ID'].drop_duplicates()

# Print result
print("Distinct Department IDs:")
print(distinct_departments)