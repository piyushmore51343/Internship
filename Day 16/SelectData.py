'''Selection and Indexing:

Select only the Name column.

Select the first 3 rows using .iloc.

Select people older than 30'''
import pandas as pd

data = {
    'Products':['Laptop','Mobile','Cars','Headphone'],
    'Price':[90999,25999,1539990,1299],
    'Stock':['5','13','3','55']

}
df = pd.DataFrame(data)
# print(df)
# print(df.to_string(index=False))

print(df['Products'])
print(df.iloc[:3])
print(df[df['Price'] > 5000])

