import numpy as np

# Input matrix
matrix = np.array([
    [6, 4],
    [8, 6]
])

# Flatten
flatten_output = matrix.flatten()

print("Flatten Output:", flatten_output)

# Example fully connected layer (manual)
weights = np.array([0.5, 0.2, 0.1, 0.7])
bias = 1

output = np.dot(flatten_output, weights) + bias

print("Final Output (Fully Connected):", output)