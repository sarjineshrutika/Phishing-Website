import pandas as pd
df=pd.read_excel(r"C:\Users\Asus\Downloads\dataset_phishing.xlsx")
import os
os.makedirs(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\raw_data",exist_ok=True)
df.to_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\raw_data\raw_data.csv",index=False)