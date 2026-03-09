import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousAdvAgency(Datapath):

    border="-"*40
    #Step 1: Get Data
    print(border)
    print("Step 1: Get Data")
    print(border)
    df = pd.read_csv(Datapath)
    print(df.head())
    #Step 2: Clean,Prepare and Manipulate the Data
    print(border)
    print("Step 2: Clean,Prepare and Manipulate the Data")
    print(border)
    print("missing values count :\n",df.isnull().sum())

    X= df[['TV','radio','newspaper']]
    Y= df['sales']

    print("Shape of independent varibale :",X.shape)
    print("Shape of dependent varibale :",Y.shape)

    X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.5,random_state=42)
    print("Shape of X_train: ",X_train.shape)
    print("Shape of X_test: ",X_test.shape)
    print("Shape of Y_train: ",Y_train.shape)
    print("Shape of Y_test: ",Y_test.shape)

    #Step 3: Train Data
    print(border)
    print("Step 3: Train Data")
    print(border)

    model= LinearRegression()
    model.fit(X_train,Y_train)

    #Step 4: Test Data
    print(border)
    print("Step 4: Test Data")
    print(border)

    Y_pred= model.predict(X_test)

    #Step 5: Visual Representation
    print(border)
    print("Step 5: Visual Representation")
    print(border)
    
    print(df.describe())

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual values")
    plt.ylabel("Predicated values")
    plt.title("Linear Regression")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvAgency("Advertising.csv")
if __name__ == "__main__":
    main()    
