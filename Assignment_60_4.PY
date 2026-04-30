x = 2
w = 0.5
b = 0.1
y_true = 1
lr = 0.01

y_pred = w*x + b
error = y_true - y_pred

w_new = w + lr * error * x

print("Old Weight:", w)
print("Updated Weight:", w_new)