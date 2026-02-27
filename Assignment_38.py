import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

#########################################################
# Step 1 : Load the dataset
#########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully...\n")

print("First 5 records")
print(df.head())

print("\nLast 5 records")
print(df.tail())

print("\nShape of dataset :", df.shape)
print("Column names :", list(df.columns))

print("\nData Types")
print(df.dtypes)


#########################################################
# Step 2 : Basic Analysis
#########################################################

print(Border)
print("Step 2 : Student Count Analysis")
print(Border)

total_students = len(df)
pass_count = df["FinalResult"].value_counts().get(1, 0)
fail_count = df["FinalResult"].value_counts().get(0, 0)

print("Total students :", total_students)
print("Students Passed :", pass_count)
print("Students Failed :", fail_count)


#########################################################
# Step 3 : Statistical Calculations
#########################################################

print(Border)
print("Step 3 : Statistical Analysis")
print(Border)

print("Average StudyHours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum PreviousScore :", df["PreviousScore"].max())
print("Minimum SleepHours :", df["SleepHours"].min())


#########################################################
# Step 4 : FinalResult Distribution
#########################################################

print(Border)
print("Step 4 : Class Distribution")
print(Border)

distribution = df["FinalResult"].value_counts()
print(distribution)

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("Pass % :", pass_percentage)
print("Fail % :", fail_percentage)

if abs(pass_percentage - fail_percentage) < 10:
    print("Dataset is approximately Balanced")
else:
    print("Dataset is Imbalanced")


#########################################################
# Step 5 : Observational Analysis
#########################################################

print(Border)
print("Step 5 : Observations")
print(Border)

print("Students with higher StudyHours generally show higher pass rates.")
print("Higher Attendance percentage appears positively correlated with FinalResult.")
print("Students scoring high in PreviousScore tend to pass again.")
print("Completing more assignments increases probability of passing.")
print("SleepHours alone does not guarantee success but moderate sleep helps.")


#########################################################
# Step 6 : Histogram - StudyHours
#########################################################

plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


#########################################################
# Step 7 : Scatter Plot
#########################################################

plt.figure(figsize=(6,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    plt.scatter(
        temp["StudyHours"],
        temp["PreviousScore"],
        label="Pass" if result==1 else "Fail"
    )

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.grid(True)
plt.show()


#########################################################
# Step 8 : Boxplot - Attendance
#########################################################

plt.figure(figsize=(5,4))
sns.boxplot(y=df["Attendance"])
plt.title("Boxplot of Attendance")
plt.show()


#########################################################
# Step 9 : Assignments vs FinalResult
#########################################################

plt.figure(figsize=(6,4))
sns.barplot(x="FinalResult", y="AssignmentsCompleted", data=df)
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()


#########################################################
# Step 10 : SleepHours vs FinalResult
#########################################################

plt.figure(figsize=(6,4))
sns.boxplot(x="FinalResult", y="SleepHours", data=df)
plt.title("SleepHours vs FinalResult")
plt.show()

print("Observation:")
print("Sleeping more does not guarantee passing.")
print("Very low sleep may negatively affect performance.")


#########################################################
# Step 11 : Build ML Model
#########################################################

print(Border)
print("Step 11 : Build & Train Model")
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)


#########################################################
# Step 12 : Model Evaluation
#########################################################

print("Accuracy :", accuracy_score(Y_test, Y_pred)*100)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix")
print(cm)

print("Classification Report")
print(classification_report(Y_test, Y_pred))

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix - Student Performance")
plt.show()