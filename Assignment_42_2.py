import matplotlib.pyplot as plt

def main():

    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    n = len(X)

    mean_x = sum(X)/n
    mean_y = sum(Y)/n

    num = 0
    den = 0

    for i in range(n):
        num = num + (X[i]-mean_x)*(Y[i]-mean_y)
        den = den + (X[i]-mean_x)**2

    m = num/den
    c = mean_y - m*mean_x

    print("Slope =",m)
    print("Intercept =",c)

    # Predict salary for 6 years experience
    x = 6
    y = m*x + c

    print("Predicted Salary for 6 years =",y)

    y_pred = []
    for i in X:
        y_pred.append(m*i + c)

    plt.scatter(X,Y)
    plt.plot(X,y_pred)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Linear Regression")
    plt.show()


if __name__ == "__main__":
    main()