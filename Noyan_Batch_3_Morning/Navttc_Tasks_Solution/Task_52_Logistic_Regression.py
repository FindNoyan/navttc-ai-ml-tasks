# Task 52 - Logistic Regression
# Sources:
#   https://towardsdatascience.com/logistic-regression-using-python-sklearn-numpy-mnist-handwriting-recognition-matplotlib-a6b31e2b166a
#   https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python
# This example shows logistic regression: predicting pass (1) or fail (0)
# from study hours and mock-test score, using scikit-learn. It trains the
# model, then checks it with accuracy and a confusion matrix.

# Idea: logistic regression is for YES/NO (binary) answers. It learns a
# boundary between the two classes. A student on one side of the
# boundary is predicted Pass (1), on the other side Fail (0).
# The target column here is 1 = Pass, 0 = Fail.

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Small inline binary dataset: 12 students.
# Columns: StudyHours, MockScore (mock-test score out of 100),
# Result (1 = Pass, 0 = Fail).
# The pattern is simple on purpose: students who studied more and
# scored higher on the mock test passed the exam.
data = {
    "StudyHours": [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 1],
    "MockScore": [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 25],
    "Result": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
}
df = pd.DataFrame(data)

# X (features, the inputs) has two columns.
# y (target, what we predict) is the Pass/Fail column.
X = df[["StudyHours", "MockScore"]]
y = df["Result"]

# Split into training data (to fit the model) and test data (to check it).
# test_size=0.25 means 25% (3 rows) are held out for testing.
# shuffle=False keeps the split in order, so the result is the same
# every time this file runs.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, shuffle=False
)

# Create the model and fit (train) it on the training data.
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict Pass/Fail for the test students.
y_pred = model.predict(X_test)

# Accuracy: fraction of test predictions that were correct.
# 1.0 means every test prediction was right.
print("Accuracy on the test data:")
print(accuracy_score(y_test, y_pred))
print()

# Confusion matrix: rows = actual class, columns = predicted class.
# [[true Fail, predicted Pass by mistake],
#  [predicted Fail by mistake, true Pass]]
# For this tiny separable dataset the model gets all 3 test rows right,
# so the off-diagonal (mistake) cells are 0.
print("Confusion matrix (rows = actual, columns = predicted):")
print(confusion_matrix(y_test, y_pred))

# Sample output:
# Accuracy on the test data:
# 1.0
#
# Confusion matrix (rows = actual, columns = predicted):
# [[1 0]
#  [0 2]]
