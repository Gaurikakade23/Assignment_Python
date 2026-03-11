import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def WineClassifier(Datapath):
    border = "-"*40
    #Step 1: Get Data
    print(border)
    print("#Step 1: Get Data")
    print(border)
    df=pd.read_csv(Datapath)
    print(df.head())

    #Step 2: Clean,Prepare and manipulate the data
    print(border)
    print("Step 2: Clean,Prepare and manipulate the data")
    print(border)
    df.dropna(inplace=True)
    X= df.drop(columns=['Class'])
    Y= df['Class']

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    #Step 3: Train Data
    print(border)
    print("Step 3: Train Data")
    print(border)
    X_train, X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)  
    print(border)
    print("Information training and testing data")
    print("X_train shape: ",X_train.shape)
    print("X_test shape: ",X_test.shape)
    print("Y_train shape: ",Y_train.shape)
    print("Y_test shape: ",Y_test.shape)

    scalar= StandardScaler()
    X_train_scaled= scalar.fit_transform(X_train)
    X_test_scaled= scalar.fit_transform(X_test)

    #Step 4: Test Data
    print(border)
    print("Step 4: Test Data")
    print(border)

    accuracy_scores =[]
    K_values =range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred=model.predict(X_test_scaled)
        accuracy= accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print(border)
    print("Accuracy report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(border)

    #Step 5: Calculate Accuracy
    print(border)
    print("tep 5: Calculate Accuracy")
    print(border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    print("best value of K is: ",best_k)
    
    final_model= KNeighborsClassifier(n_neighbors= best_k)
    final_model.fit(X_train_scaled,Y_train)
    Y_pred=final_model.predict(X_test_scaled)

    accuracy= accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is :",accuracy*100)
    
def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()    