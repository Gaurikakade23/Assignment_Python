# ===============================
# Fake News Detection Assignment
# ===============================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ===============================
# Part 1: Data Preprocessing
# ===============================

# Load datasets
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# Add labels
fake_df['label'] = 0   # Fake
true_df['label'] = 1   # Real

# Combine datasets
df = pd.concat([fake_df, true_df], axis=0)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Combine title + text
df['content'] = df['title'] + " " + df['text']

# Keep only required columns
df = df[['content', 'label']]

# Drop missing values
df = df.dropna()

# ===============================
# Part 2: Feature Extraction
# ===============================

tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

X = tfidf.fit_transform(df['content'])
y = df['label']

# ===============================
# Train-Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Part 3: Model Training
# ===============================

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# ===============================
# Voting Classifier
# ===============================

# Hard Voting
hard_voting = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='hard'
)
hard_voting.fit(X_train, y_train)

# Soft Voting
soft_voting = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='soft'
)
soft_voting.fit(X_train, y_train)

# ===============================
# Part 4: Evaluation
# ===============================

# Predictions
lr_pred = lr.predict(X_test)
dt_pred = dt.predict(X_test)
hard_pred = hard_voting.predict(X_test)
soft_pred = soft_voting.predict(X_test)

# 1. Compare Accuracies
lr_acc = accuracy_score(y_test, lr_pred)
dt_acc = accuracy_score(y_test, dt_pred)
hard_acc = accuracy_score(y_test, hard_pred)
soft_acc = accuracy_score(y_test, soft_pred)

print("\n===== Model Accuracy Comparison =====")
print("Logistic Regression Accuracy:", lr_acc)
print("Decision Tree Accuracy:", dt_acc)
print("Hard Voting Accuracy:", hard_acc)
print("Soft Voting Accuracy:", soft_acc)

# Best model
accuracies = {
    "Logistic Regression": lr_acc,
    "Decision Tree": dt_acc,
    "Hard Voting": hard_acc,
    "Soft Voting": soft_acc
}

best_model = max(accuracies, key=accuracies.get)
print("\nBest Performing Model:", best_model)

# ===============================
# 2. Confusion Matrices
# ===============================

print("\n===== Confusion Matrices =====")

print("\nLogistic Regression")
print(confusion_matrix(y_test, lr_pred))

print("\nDecision Tree")
print(confusion_matrix(y_test, dt_pred))

print("\nHard Voting")
print(confusion_matrix(y_test, hard_pred))

print("\nSoft Voting")
print(confusion_matrix(y_test, soft_pred))

# ===============================
# 3. Soft vs Hard Voting
# ===============================

print("\n===== Soft vs Hard Voting Comparison =====")

print("Hard Voting Accuracy:", hard_acc)
print("Soft Voting Accuracy:", soft_acc)

if soft_acc > hard_acc:
    print("Soft Voting performs better because it uses probability scores.")
elif hard_acc > soft_acc:
    print("Hard Voting performs better based on majority voting.")
else:
    print("Both methods perform equally.")

# ===============================
# Classification Report
# ===============================

print("\n===== Classification Report (Soft Voting) =====")
print(classification_report(y_test, soft_pred))