import numpy as np

# Input feature map
feature_map = np.array([
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
])

# ReLU function
def relu(x):
    return np.maximum(0, x)

relu_output = relu(feature_map)

print("ReLU Output:\n", relu_output)

# Max Pooling (2x2)
pool_size = 2
stride = 1

pooled_output = []

for i in range(relu_output.shape[0] - pool_size + 1):
    row = []
    for j in range(relu_output.shape[1] - pool_size + 1):
        region = relu_output[i:i+2, j:j+2]
        row.append(np.max(region))
    pooled_output.append(row)

pooled_output = np.array(pooled_output)

print("\nMax Pooled Output:\n", pooled_output)