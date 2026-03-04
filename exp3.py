import pandas as pd

# Read the CSV file
df = pd.read_csv("jobs.csv")

# Sort jobs in descending order of JOB_TITLE
sorted_jobs = df.sort_values(by='JOB_TITLE', ascending=False)

# Display result
print("Jobs in descending order of Job Title:")
print(sorted_jobs)