def main():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    n = len(X)

    # Mean of X
    mean_x = sum(X) / n

    # Mean of Y
    mean_y = sum(Y) / n

    num = 0
    den = 0

    for i in range(n):
        num = num + (X[i] - mean_x) * (Y[i] - mean_y)
        den = den + (X[i] - mean_x) ** 2

    # Slope
    m = num / den

    # Intercept
    c = mean_y - m * mean_x

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)
    print("Slope (m) =", m)
    print("Intercept (c) =", c)

    print("Regression Equation: Y =", m, "X +", c)

    # Prediction
    x = 6
    y = m * x + c

    print("Predicted Y for X = 6:", y)


if __name__ == "__main__":
    main()