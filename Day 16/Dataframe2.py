'''Inspect the DataFrame:

Use .head() and .tail() to view your data.

Use .info() and .describe() to understand the structure.'''

import pandas as pd 

data = {
    'Products':['Laptop','Mobile','Cars','Headphone','adapter','cable','charger'],
    'Price':['90999','25999','1539999','1299','500','200','800'],
    'Stock':['5','13','3','55','3','10','12']

}
df = pd.DataFrame(data)
# print(df)
print(df.to_string(index=False))
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())