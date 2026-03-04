import pandas as pd

# Create the sales_data DataFrame
sales_data = pd.DataFrame({
    'OrderDate': ['1-6-18','1-23-18','2-9-18','2-26-18','3-15-18','4-1-18',
                  '4-18-18','5-5-18','5-22-18','6-8-18','6-25-18','7-12-18',
                  '7-29-18','8-15-18','9-1-18','9-18-18','10-5-18','10-22-18'],
    'Region': ['East','Central','Central','Central','West','East',
               'Central','Central','West','East','Central','East',
               'East','East','Central','East','Central','East'],
    'Manager': ['Martha','Hermann','Hermann','Timothy','Timothy','Martha',
                'Martha','Hermann','Douglas','Martha','Hermann','Martha',
                'Douglas','Martha','Douglas','Martha','Hermann','Martha'],
    'SalesMan': ['Alexander','Shelli','Luis','David','Stephen','Alexander',
                 'Steven','Luis','Michael','Alexander','Sigal','Diana',
                 'Karen','Alexander','John','Alexander','Sigal','Alexander'],
    'Sale_amt': [113810,25000,43128,6075,67088,30000,
                 89850,107820,38336,30000,107820,14500,
                 40500,41930,250,936,14000,14400]
})

# Create Pivot Table
pivot_table = pd.pivot_table(
    sales_data,
    values='Sale_amt',
    index=['Region','Manager','SalesMan'],
    aggfunc='sum'
)

print(pivot_table)