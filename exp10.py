import pandas as pd
import numpy as np

# Create dataframe with random values
np.random.seed(0)   # For reproducibility
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['A', 'B', 'C', 'D'])

# Function to color negative and positive numbers
def color_values(val):
    if val < 0:
        return 'color: red'
    else:
        return 'color: black'

# Apply styling
styled_df = df.style.applymap(color_values)

styled_df