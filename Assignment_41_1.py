import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def main():

    dataset = [
        {'X':1, 'Y':2, 'Class':"Red"},
        {'X':2, 'Y':3, 'Class':"Red"},
        {'X':3, 'Y':1, 'Class':"Blue"},
        {'X':6, 'Y':5, 'Class':"Blue"}
    ]

    X = int(input("Enter X coordinate: "))
    Y = int(input("Enter Y coordinate: "))

    new_point = {'X':X, 'Y':Y}

    # Calculate distance
    for d in dataset:
        d['distance'] = EucDistance(d, new_point)

    border = "-" * 20

    print(border)
    print("Calculated distances are:")
    print(border)

    for d in dataset:
        print(d)

    # Sort data
    sorted_data = sorted(dataset, key=lambda item: item['distance'])

    print(border)
    print("Sorted data is:")
    print(border)

    for d in sorted_data:
        print(d)

    # Select K nearest neighbors
    k = 3
    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 elements are:")
    print(border)

    for d in nearest:
        print(d)

    # Majority voting
    red = 0
    blue = 0

    for d in nearest:
        if d['Class'] == "Red":
            red += 1
        else:
            blue += 1

    print(border)

    if red > blue:
        print("Predicted Class: Red")
    else:
        print("Predicted Class: Blue")

    print(border)


if __name__ == "__main__":
    main()