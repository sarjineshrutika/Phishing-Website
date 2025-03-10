from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier




params = {
    "LogisticRegression()": {
        "penalty": ["l1", "l2", "elasticnet", None],
        "C": [0.01, 0.1, 1, 10, 100],
        "solver": ["liblinear", "lbfgs", "saga"],
        "max_iter": [100, 200, 500]
    },
    "DecisionTreeClassifier()": {
        "criterion": ["gini", "entropy", "log_loss"],
        "splitter": ["best", "random"],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    },
    "RandomForestClassifier()": {
        "n_estimators": [50, 100, 200],
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "bootstrap": [True, False]
    }
}

import joblib
model = joblib.load(r'C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\models\model')
model
params = params[str(model)]
params

from sklearn.model_selection import GridSearchCV # use for hyperparameter
import pandas as pd

x_test=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_test.csv")
x_train=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\x_train.csv")
y_train=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_train.csv")
y_test=pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\data\preprocess_data\y_test.csv")
best_estimators = {}

grid_search = GridSearchCV(model, params, cv=5, scoring="accuracy", n_jobs=-1)
grid_search.fit(x_train, y_train)
best_estimators = grid_search.best_estimator_
print(f"Best parameters for : {grid_search.best_params_}")

# Evaluate on test set
accuracy = model.score(x_test, y_test)
print(f"Test Accuracy for : {accuracy:.4f}")

best_model=grid_search.best_estimator_
joblib.dump(best_model,r"C:\Users\Asus\OneDrive\Desktop\Ml Bootcamp\models\best_model")