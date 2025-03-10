import pandas as pd
x_train=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_train.csv")
x_train.head()
x_test=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_test.csv")
x_test.head()
y_train=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_train.csv")
y_train.head()
y_test=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_test.csv")
y_test.head()
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
models = [LogisticRegression(),DecisionTreeClassifier(),RandomForestClassifier()]
d = {}
for i in models:
    i.fit(x_train, y_train)
    pred = i.predict(x_test)
    ac = accuracy_score(y_test, pred)
    if i not in d:
        d[i]=ac
d
model = [a for a,b in d.items() if b ==max(d.values())][0]
model
import joblib
joblib.dump(model, r'C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\models\best_model')