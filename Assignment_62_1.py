import numpy as np

# Input image (5x5)
image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# Kernel (3x3 edge detector)
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

# Output feature map size
output_size = image.shape[0] - kernel.shape[0] + 1
feature_map = np.zeros((output_size, output_size))

print("=== Convolution Steps ===\n")

# Perform convolution
for i in range(output_size):
    for j in range(output_size):
        region = image[i:i+3, j:j+3]
        result = np.sum(region * kernel)
        feature_map[i][j] = result

        print(f"Region ({i},{j}):\n{region}")
        print(f"Result: {result}\n")

print("Feature Map:\n", feature_map)