import pandas as pd
df = pd.read_csv(r'C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\raw_data\raw_data.csv')
df.isnull().sum()
df.drop('url',axis=1,inplace=True)
import os
os.makedirs(r'C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\cleaned_data',exist_ok=True)
df.to_csv(r'C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\cleaned_data\cleaned.csv',index=False)