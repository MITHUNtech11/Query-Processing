import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

# Count number of jobs per employee
job_counts = df.groupby('EMPLOYEE_ID').size()

# Select employees who have done 2 or more jobs
employees_multiple_jobs = job_counts[job_counts >= 2].index

# Display result
print("Employees who have done two or more jobs:")
print(employees_multiple_jobs)