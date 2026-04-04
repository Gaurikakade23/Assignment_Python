# ==========================================
# Step 1: Import Libraries
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# Step 2: Load Dataset
# ==========================================
df = pd.read_csv("diabetes.csv")

print("First 5 rows:\n", df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:\n", df.isnull().sum())

print("\nStatistical Summary:\n", df.describe())

# ==========================================
# Step 3: Exploratory Data Analysis (EDA)
# ==========================================

# Target variable distribution
sns.countplot(x='Outcome', data=df)
plt.title("Distribution of Diabetes Outcome")
plt.show()

# Histograms
df.hist(figsize=(10,10))
plt.show()

# Boxplot (to detect outliers)
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

# ==========================================
# Step 4: Data Preprocessing
# ==========================================

# Replace zero values with median
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in cols:
    df[col] = df[col].replace(0, df[col].median())

# Features and Target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# ==========================================
# Step 5: Model Building
# ==========================================

# Initialize Models
lr = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors=5)
dt = DecisionTreeClassifier()

# Train Models
lr.fit(X_train, y_train)
knn.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Predictions
y_pred_lr = lr.predict(X_test)
y_pred_knn = knn.predict(X_test)
y_pred_dt = dt.predict(X_test)

# ==========================================
# Step 6: Model Evaluation
# ==========================================

print("\n===== Logistic Regression =====")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_lr))
print("Classification Report:\n", classification_report(y_test, y_pred_lr))

print("\n===== KNN =====")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn))

print("\n===== Decision Tree =====")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))
print("Classification Report:\n", classification_report(y_test, y_pred_dt))

# ==========================================
# Step 7: Confusion Matrix Visualization
# ==========================================

plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred_lr), annot=True, fmt='d')
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ==========================================
# Step 8: Final Output (Predictions)
# ==========================================

# Using best model (Logistic Regression)
predictions = lr.predict(X_test)

# Display predictions
print("\nSample Predictions:\n", predictions[:10])

# Save to CSV
output = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions
})

output.to_csv("diabetes_predictions.csv", index=False)

print("\nPredictions saved to 'diabetes_predictions.csv'")