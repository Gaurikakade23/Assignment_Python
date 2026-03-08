import math

def EuclideanDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def Predict(data, new_point, k):
    distances = []

    # Calculate distance from new point to each data point
    for point in data:
        dist = EuclideanDistance(point[0], new_point)
        distances.append((dist, point[1]))

    # Sort distances
    distances.sort()

    # Select K nearest neighbors
    neighbors = distances[:k]

    # Majority voting
    count = {}
    for n in neighbors:
        label = n[1]
        if label in count:
            count[label] += 1
        else:
            count[label] = 1

    # Find label with maximum votes
    prediction = max(count, key=count.get)
    return prediction


def main():
    # Dataset
    data = [
        ((1,2),'Red'),
        ((2,3),'Red'),
        ((3,1),'Blue'),
        ((6,5),'Blue')
    ]

    # New point to classify
    new_point = (3,3)

    print("Prediction Results")

    k1 = Predict(data, new_point, 1)
    print("K = 1 :", k1)

    k3 = Predict(data, new_point, 3)
    print("K = 3 :", k3)

    k5 = Predict(data, new_point, 5)
    print("K = 5 :", k5)


if __name__ == "__main__":
    main()