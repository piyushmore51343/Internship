'''Create a DataFrame:

Create a DataFrame with columns: Products, Price, and Stock.

Add 5 sample rows.'''

import pandas as pd

data = {
    'Products':['Laptop','Mobile','Cars','Headphone'],
    'Price':['90999','25999','1539999','1299'],
    'Stock':['5','13','3','55']

}
df = pd.DataFrame(data)
# print(df)
print(df.to_string(index=False))