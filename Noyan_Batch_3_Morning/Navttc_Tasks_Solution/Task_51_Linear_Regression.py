# Task 51 - Linear Regression
# Source: https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
# This example shows linear regression: predicting exam marks (a number)
# from study hours, using scikit-learn. It trains a straight-line model,
# checks it with an R^2 score, and predicts marks for a new input.

# Idea: linear regression fits the straight line
#     marks = coefficient * study_hours + intercept
# that best matches the training data. The coefficient is the slope
# (how many extra marks each extra study hour is worth), and the
# intercept is where the line crosses the vertical axis.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Small inline dataset: 10 students, study hours -> exam marks.
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 45, 52, 58, 63, 68, 74, 80, 88]
}
df = pd.DataFrame(data)

# X (features, the input) must be 2D: one column in double brackets.
# y (target, what we predict) is one column.
X = df[["StudyHours"]]
y = df["Marks"]

# Split into training data (to fit the model) and test data (to check it).
# test_size=0.2 means 20% (2 rows) are held out for testing.
# shuffle=False keeps the split in order, so the result is the same
# every time this file runs.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Create the model and fit (train) it on the training data.
model = LinearRegression()
model.fit(X_train, y_train)

# The fitted line: Marks = coefficient * StudyHours + intercept.
print("Coefficient (slope - marks gained per extra study hour):")
print(model.coef_[0])
print()
print("Intercept (predicted marks at 0 study hours):")
print(model.intercept_)
print()

# Check the model on the test data.
# R^2 is between 0 and 1 (higher is better): 1.0 would mean the line
# predicts the test marks perfectly.
y_pred = model.predict(X_test)
print("R^2 score on the test data:")
print(r2_score(y_test, y_pred))
print()

# Predict for a new student who studied 6.5 hours.
new_hours = [[6.5]]
predicted_marks = model.predict(new_hours)
print("Predicted marks for a student who studied 6.5 hours:")
print(predicted_marks[0])

# Sample output:
# Coefficient (slope - marks gained per extra study hour):
# 5.630952380952381
#
# Intercept (predicted marks at 0 study hours):
# 29.035714285714285
#
# R^2 score on the test data:
# 0.7772064554988675
#
# Predicted marks for a student who studied 6.5 hours:
# 65.63690476190476
