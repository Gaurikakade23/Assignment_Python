# ================================
# Step 1: Import Libraries
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ================================
# Step 2: Load Dataset
# ================================
# IMPORTANT: Dataset uses ';' separator
df = pd.read_csv("student-mat.csv", sep=';')

# ================================
# Step 3: Select Required Features
# ================================
features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
data = df[features].copy()

# ================================
# Step 4: Handle Missing Values
# ================================
data = data.dropna()

# ================================
# Step 5: Feature Scaling
# ================================
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# ================================
# Step 6: Apply K-Means Clustering
# ================================
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels
data['Cluster'] = clusters

# ================================
# Step 7: Analyze Cluster Centers
# ================================
centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers = pd.DataFrame(centers, columns=features)

print("\nCluster Centers:\n")
print(cluster_centers)

# ================================
# Step 8: Assign Meaningful Labels
# ================================
# Add cluster index properly
cluster_centers['Cluster'] = range(len(cluster_centers))

# Sort by final grade (G3)
cluster_centers = cluster_centers.sort_values(by='G3', ascending=False)

# Create labels
labels = {}
labels[int(cluster_centers.iloc[0]['Cluster'])] = "Top Performers"
labels[int(cluster_centers.iloc[1]['Cluster'])] = "Average Students"
labels[int(cluster_centers.iloc[2]['Cluster'])] = "Struggling Students"

# Map labels
data['Performance'] = data['Cluster'].map(labels)

# ================================
# Step 9: Display Results
# ================================
print("\nSample Clustered Data:\n")
print(data[['G1','G2','G3','studytime','failures','absences','Performance']].head())

print("\nCluster Distribution:\n")
print(data['Performance'].value_counts())

# ================================
# Step 10: Visualization
# ================================
plt.figure(figsize=(8,6))

for label in data['Performance'].unique():
    subset = data[data['Performance'] == label]
    plt.scatter(subset['G3'], subset['studytime'], label=label)

plt.xlabel("Final Grade (G3)")
plt.ylabel("Study Time")
plt.title("Student Performance Clusters")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()