import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

print("-"*60)
print("STUDENT PERFORMANCE - DECISION TREE ANALYSIS")
print("-"*60)

#########################################################
# STEP 1: Load Dataset and Train Basic Model
#########################################################

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours","Attendance","PreviousScore",
        "AssignmentsCompleted","SleepHours"]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("\nSTEP 1: Model trained successfully")

#########################################################
# STEP 2: Feature Importance
#########################################################

print("\nSTEP 2: Feature Importance")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print(importance)

#########################################################
# STEP 3: Remove SleepHours and Retrain
#########################################################

X_no_sleep = df[["StudyHours","Attendance",
                 "PreviousScore","AssignmentsCompleted"]]

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X_no_sleep, Y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train2, Y_train2)

acc_no_sleep = model2.score(X_test2, Y_test2)

print("\nSTEP 3: Accuracy without SleepHours:", acc_no_sleep*100)

#########################################################
# STEP 4: Train Using Only StudyHours & Attendance
#########################################################

X_small = df[["StudyHours","Attendance"]]

X_train3, X_test3, Y_train3, Y_test3 = train_test_split(
    X_small, Y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(max_depth=3, random_state=42)
model3.fit(X_train3, Y_train3)

acc_small = model3.score(X_test3, Y_test3)

print("\nSTEP 4: Accuracy with 2 features:", acc_small*100)

#########################################################
# STEP 5: Predict 5 New Students
#########################################################

new_students = pd.DataFrame({
    "StudyHours":[5,8,2,6,4],
    "Attendance":[80,92,60,85,70],
    "PreviousScore":[65,88,40,72,55],
    "AssignmentsCompleted":[6,9,2,7,4],
    "SleepHours":[7,6,8,7,5]
})

predictions = model.predict(new_students)
new_students["PredictedResult"] = predictions

print("\nSTEP 5: New Student Predictions")
print(new_students)

#########################################################
# STEP 6: Manual Accuracy Calculation
#########################################################

correct = 0
for i in range(len(Y_test)):
    if Y_test.values[i] == Y_pred[i]:
        correct += 1

manual_accuracy = correct / len(Y_test)

print("\nSTEP 6: Manual Accuracy:", manual_accuracy*100)
print("Sklearn Accuracy:", accuracy_score(Y_test, Y_pred)*100)

#########################################################
# STEP 7: Misclassified Students
#########################################################

misclassified = X_test[Y_test != Y_pred]

print("\nSTEP 7: Misclassified Students")
print(misclassified)
print("Total Misclassified:", len(misclassified))

#########################################################
# STEP 8: Random State Comparison
#########################################################

print("\nSTEP 8: Random State Comparison")

for state in [0,10,42]:
    X_train_s, X_test_s, Y_train_s, Y_test_s = train_test_split(
        X, Y, test_size=0.2, random_state=state
    )
    
    temp_model = DecisionTreeClassifier(max_depth=3, random_state=state)
    temp_model.fit(X_train_s, Y_train_s)
    
    acc = temp_model.score(X_test_s, Y_test_s)
    print("Random State", state, "Accuracy:", acc*100)

#########################################################
# STEP 9: Decision Tree Visualization
#########################################################

print("\nSTEP 9: Decision Tree Visualization")

plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns,
          class_names=["Fail","Pass"],
          filled=True)
plt.show()

#########################################################
# STEP 10: Add PerformanceIndex & Overfitting Check
#########################################################

df["PerformanceIndex"] = (df["StudyHours"]*2) + df["Attendance"]

X_new = df[["StudyHours","Attendance","PreviousScore",
            "AssignmentsCompleted","SleepHours",
            "PerformanceIndex"]]

X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new, Y, test_size=0.2, random_state=42
)

model_new = DecisionTreeClassifier(max_depth=3, random_state=42)
model_new.fit(X_train_new, Y_train_new)

print("\nSTEP 10: Accuracy with PerformanceIndex:",
      model_new.score(X_test_new, Y_test_new)*100)

# Overfitting check
deep_model = DecisionTreeClassifier(max_depth=None, random_state=42)
deep_model.fit(X_train, Y_train)

print("Deep Tree Training Accuracy:",
      deep_model.score(X_train, Y_train)*100)

print("Deep Tree Testing Accuracy:",
      deep_model.score(X_test, Y_test)*100)

print("\nPROGRAM COMPLETED SUCCESSFULLY")