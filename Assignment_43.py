import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def MarvellousPlayPredictor():

    border = "-" * 50
    
    # Step 1 : Get Data
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv("PlayPredictor.csv")
    print(df.head())

    # Step 2 : Clean, Prepare and Manipulate Data
    print(border)
    print("Step 2 : Data Preparation")
    print(border)

    le_whether = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_whether.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    print(df)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    # Step 3 : Train Data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)

    # Step 4 : Test Data
    print(border)
    print("Step 4 : Test Data")
    print(border)

    Whether = input("Enter Whether (Sunny/Overcast/Rainy): ")
    Temperature = input("Enter Temperature (Hot/Mild/Cool): ")

    w = le_whether.transform([Whether])[0]
    t = le_temp.transform([Temperature])[0]

    prediction = model.predict([[w,t]])

    result = le_play.inverse_transform(prediction)

    print("Prediction is :", result[0])


def CheckAccuracy():

    print("\nChecking Accuracy\n")

    df = pd.read_csv("PlayPredictor.csv")

    le_whether = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_whether.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    X = df[['Whether','Temperature']]
    Y = df['Play']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

    for k in range(1,8):

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test,Y_pred)

        print("Accuracy with K =",k,"is :",acc)


def main():

    MarvellousPlayPredictor()
    CheckAccuracy()


if __name__ == "__main__":
    main()