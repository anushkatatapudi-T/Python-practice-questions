import pandas as pd
df=pd.read_csv('days.csv')
df=df.query('days==days.min()')
print(df)