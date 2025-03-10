import pandas as pd
df=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\cleaned_data\cleaned.csv")
df.head()
df.info()


x = df.drop('status',axis=1)
y = df['status']


# Feature Selection
from sklearn.feature_selection import SelectKBest, f_classif

# Select top 10 best features
selector = SelectKBest(score_func=f_classif, k=10)
x_new = selector.fit_transform(x, y)

# Get selected feature names
selected_features = x.columns[selector.get_support()]
print("Selected Features:", selected_features)

# split data in train test split
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=42,stratify=y)

import os
os.makedirs(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data",exist_ok=True)

x_train.to_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_train.csv",index=False)
x_test.to_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_test.csv",index=False)
y_train.to_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_train.csv",index=False)
y_test.to_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_test.csv",index=False)
