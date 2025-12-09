import pandas as pd

data = {'Name':['A','B','C'], 'Marks':[90, None, 70]}
df = pd.DataFrame(data)
print(df.fillna(method='bfill'))
