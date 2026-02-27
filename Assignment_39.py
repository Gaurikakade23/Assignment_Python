import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

print("-"*50)
print("STUDENT PERFORMANCE PREDICTION SYSTEM")
print("-"*50)

#########################################################
# 1. DATASET LOADING
#########################################################

df = pd.read_csv("student_performance_ml.csv")

print("First 5 records")
print(df.head())

print("Dataset Shape:", df.shape)
print("Columns:", list(df.columns))

#########################################################
# 2. DATA ANALYSIS
#########################################################

print("\nPass/Fail Distribution")
print(df["FinalResult"].value_counts())

print("\nStatistical Summary")
print(df.describe())

#########################################################
# 3. VISUALIZATION
#########################################################

plt.figure(figsize=(6,4))
sns.histplot(df["StudyHours"], bins=10, kde=True)
plt.title("Study Hours Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="StudyHours", y="PreviousScore",
                hue="FinalResult", data=df)
plt.title("StudyHours vs PreviousScore")
plt.show()

#########################################################
# 4. TRAIN-TEST SPLIT
#########################################################

X = df[["StudyHours","Attendance","PreviousScore",
        "AssignmentsCompleted","SleepHours"]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

#########################################################
# 5. MODEL TRAINING
#########################################################

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, Y_train)

#########################################################
# 6. PREDICTION
#########################################################

Y_pred = model.predict(X_test)

print("\nActual Values")
print(Y_test.values)

print("\nPredicted Values")
print(Y_pred)

#########################################################
# 7. ACCURACY CALCULATION
#########################################################

train_acc = model.score(X_train, Y_train)
test_acc = model.score(X_test, Y_test)

print("\nTraining Accuracy: {:.2f}%".format(train_acc*100))
print("Testing Accuracy: {:.2f}%".format(test_acc*100))

#########################################################
# 8. CONFUSION MATRIX
#########################################################

cm = confusion_matrix(Y_test, Y_pred)
print("\nConfusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix - Student Performance")
plt.show()

print("\nClassification Report")
print(classification_report(Y_test, Y_pred))

#########################################################
# 9. FINAL CONCLUSION
#########################################################

if train_acc > test_acc + 0.10:
    print("Model is Overfitting")
elif train_acc < test_acc:
    print("Model is Underfitting")
else:
    print("Model is Well Balanced")

#########################################################
# Predict New Student
#########################################################

new_student = [[6,85,66,7,7]]
result = model.predict(new_student)

if result[0] == 1:
    print("\nNew Student Prediction: PASS")
else:
    print("\nNew Student Prediction: FAIL")