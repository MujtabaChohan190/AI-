import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
iris = datasets.load_iris()
X = iris.data          # Features (150 × 4)
y = iris.target        # Labels (0, 1, 2)

# Convert to binary classification (Setosa vs NOT Setosa)
y = (y == 0).astype(int)   # 1 = Setosa, 0 = Others

# ---------------- SPLIT DATA ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ---------------- CREATE MODEL ----------------
svm = SVC(kernel='rbf', C=1, gamma='scale')  
# kernel='rbf' → handles non-linear data
# C → controls margin vs misclassification
# gamma → controls influence of points

# ---------------- TRAIN MODEL ----------------
svm.fit(X_train, y_train)

# ---------------- PREDICT ----------------
y_pred = svm.predict(X_test)

# ---------------- EVALUATE ----------------
print("SVM Accuracy:", accuracy_score(y_test, y_pred))

SVM ACCURACY - ACCURACY_SCORE
LINEAR -  R2 SCORE ,


------------------------------------------




import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ---------------- LOAD DATA ----------------
# Example dummy data (replace with your dataset)
# X = features, y = continuous values
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# ---------------- SPLIT DATA ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- CREATE MODEL ----------------
lr = LinearRegression()

# ---------------- TRAIN MODEL ----------------
lr.fit(X_train, y_train)

# ---------------- PREDICT ----------------
y_pred = lr.predict(X_test)

# ---------------- EVALUATE ----------------
print("Predictions:", y_pred)
print("MSE:", mean_squared_error(y_test, y_pred))



------------------------------------------------------------------

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ---------------- LOAD DATA ----------------
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# ---------------- SPLIT DATA ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- CREATE MODEL ----------------
lr = LinearRegression()

# ---------------- TRAIN MODEL ----------------
lr.fit(X_train, y_train)

# ---------------- PREDICT ----------------
y_pred = lr.predict(X_test)

# ---------------- EVALUATE ----------------

# 1. Mean Squared Error (actual regression metric)
mse = mean_squared_error(y_test, y_pred)

# 2. R² Score
r2 = r2_score(y_test, y_pred)

# 3. "Accuracy" style (R² in percentage form)
accuracy = r2 * 100

print("Predictions:", y_pred)
print("MSE:", mse)
print("R2 Score:", r2)
print("LR Testing Accuracy (%):", accuracy)



--------------------------



import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
# Example dummy data (replace with your dataset)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 1, 0, 1, 0])   # Binary classes

# ---------------- SPLIT DATA ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- CREATE MODEL ----------------
dt = DecisionTreeClassifier()

# ---------------- TRAIN MODEL ----------------
dt.fit(X_train, y_train)

# ---------------- PREDICT ----------------
y_pred = dt.predict(X_test)

# ---------------- EVALUATE ----------------

# Predictions
print("Predictions:", y_pred)

# Training Accuracy
train_acc = dt.score(X_train, y_train) * 100
print("DT Training Accuracy (%):", train_acc)

# Testing Accuracy
test_acc = accuracy_score(y_test, y_pred) * 100
print("DT Testing Accuracy (%):", test_acc)
