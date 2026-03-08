import math

def Distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def Predict(data, new_point, k):
    distances = []

    for point in data:
        dist = Distance(point[0], new_point)
        distances.append((dist, point[1]))

    distances.sort()

    neighbors = distances[:k]

    count = {}
    for n in neighbors:
        label = n[1]
        if label in count:
            count[label] += 1
        else:
            count[label] = 1

    prediction = max(count, key=count.get)
    return prediction


def main():
    # Dataset (Study Hours, Attendance, Result)
    data = [
        ((2,60),'Fail'),
        ((4,80),'Pass'),
        ((6,85),'Pass'),
        ((3,50),'Fail')
    ]

    study = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    new_point = (study, attendance)

    k = 3

    result = Predict(data, new_point, k)

    print("Prediction:", result)


if __name__ == "__main__":
    main()