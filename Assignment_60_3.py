import numpy as np

y_true = np.array([1, 0, 1, 1])
y_pred = np.array([0.9, 0.2, 0.8, 0.7])

mse = np.mean((y_true - y_pred)**2)
bce = -np.mean(y_true*np.log(y_pred) + (1-y_true)*np.log(1-y_pred))

print("MSE:", mse)
print("Binary Cross Entropy:", bce)