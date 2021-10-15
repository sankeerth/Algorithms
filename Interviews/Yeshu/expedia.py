# Metroland festival hackerrank

def minimizeCost(numPeople, x, y):
    def distance(xFest, yFest, xCity, yCity):
        return abs(xFest-xCity) + abs(yFest-yCity)

    res = 0
    xCoordsSorted, yCoordsSorted = [], []

    for i in range(len(numPeople)):
        num = numPeople[i]
        for j in range(num):
            xCoordsSorted.append(x[i])
            yCoordsSorted.append(y[i])

    xCoordsSorted.sort()
    yCoordsSorted.sort()
    
    xFest, yFest = xCoordsSorted[len(xCoordsSorted) // 2], yCoordsSorted[len(yCoordsSorted) // 2]

    for i in range(len(numPeople)):
        num = numPeople[i]
        dist = distance(xFest, yFest, x[i], y[i])
        res += num * dist

    return res
    

