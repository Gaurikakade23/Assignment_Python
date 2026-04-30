import math

x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

z = x1*w1 + x2*w2 + bias
output = 1 / (1 + math.exp(-z))

print("Weighted Sum:", z)
print("Final Output:", output)