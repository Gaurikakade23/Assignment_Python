# ================================
# Step 1: Import Libraries
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ================================
# Step 2: Load Dataset 
# ================================
df = pd.read_csv("bank-full.csv", sep=';')

# Display first few rows
print("First 5 Rows:\n", df.head())

# Dataset information
print("\nDataset Info:\n")
print(df.info())

# Missing values
print("\nMissing Values:\n", df.isnull().sum())

# ================================
# Step 3: Data Visualization
# ================================

plt.figure()
sns.countplot(x='y', data=df)
plt.title("Target Variable Distribution")
plt.show()

# Histogram for numerical features
df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()

# Age distribution
plt.figure()
sns.histplot(df['age'], kde=True)
plt.title("Age Distribution")
plt.show()

# ================================
# Step 4: Data Preprocessing
# ================================

# Convert target variable (yes/no → 1/0)
df['y'] = df['y'].map({'yes': 1, 'no': 0})

# Convert categorical variables to numeric
df_encoded = pd.get_dummies(df, drop_first=True)

# Check columns
print("\nEncoded Columns:\n", df_encoded.columns)

# Split features and target
X = df_encoded.drop('y', axis=1)
y = df_encoded['y']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ================================
# Step 5: Train Models
# ================================

# Logistic Regression
lr = LogisticRegression(max_iter=2000)
lr.fit(X_train, y_train)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Gradient Boosting
gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)

# ================================
# Step 6: Evaluate Models
# ================================

models = {
    "Logistic Regression": lr,
    "Random Forest": rf,
    "Gradient Boosting": gb
}

accuracies = {}

for name, model in models.items():
    print("\n===============================")
    print(f"Model: {name}")
    
    y_pred = model.predict(X_test)
    
    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    accuracies[name] = acc
    print("Accuracy:", acc)
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)
    
    # Classification Report
    cr = classification_report(y_test, y_pred)
    print("Classification Report:\n", cr)

# ================================
# Step 7: Compare Results
# ================================

print("\n===== Model Accuracy Comparison =====")
for model, acc in accuracies.items():
    print(f"{model}: {acc}")

# Best model
best_model = max(accuracies, key=accuracies.get)
print("\nBest Performing Model:", best_model)

# ================================
# Step 8: Accuracy Visualization
# ================================

plt.figure()
plt.bar(accuracies.keys(), accuracies.values())
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print("\nModel Comparison Completed!")