import pandas as pd

df = pd.DataFrame({
    'Name': ['Amit', 'Neha', None],
    'Marks': [85, None, 90]
})

print(df.isnull())