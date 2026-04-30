from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

X = [
 [25,500,12,1,2],[30,700,24,0,1],[45,1200,6,5,8],
 [50,1500,5,6,10],[28,600,18,1,1],[35,800,30,0,0],
 [48,1400,4,7,9],[52,1600,3,8,12],[27,550,20,0,1],
 [42,1300,8,4,7]
]

y = [0,0,1,1,0,0,1,1,0,1]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=500)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

new_customer = scaler.transform([[46,1450,5,6,9]])
pred = model.predict(new_customer)

print("Prediction:", "Customer may leave" if pred[0]==1 else "Customer will stay")