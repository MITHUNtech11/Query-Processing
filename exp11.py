import pandas as pd
import numpy as np

# Step 1: Create DataFrame with random values
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'])

# Step 2: Convert some values to NaN
df.iloc[0,1] = np.nan
df.iloc[3,2] = np.nan
df.iloc[5,0] = np.nan
df.iloc[9,3] = np.nan

# Step 3: Function to highlight NaN values
def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: red'
    else:
        return ''

# Step 4: Display highlighted DataFrame
highlighted_df = df.style.applymap(highlight_nan)

print(df)
highlighted_df