distance=0
lapCount=0
amountOfLaps=0

testCases = int(input())
for testCasesIndex in range(testCases):
    trackSize, inputsRan = map(int, input().split())
    for inputsRanIndex in range(inputsRan):
        unitsRan, direction = input().split()
        unitsRan = int(unitsRan)

        if direction == 'C':
            distance+=unitsRan
        else:
            distance-=unitsRan

        if distance >= trackSize:
            amountOfLaps = distance//trackSize
            lapCount += amountOfLaps
            distance -= amountOfLaps*trackSize
        elif distance <= -trackSize:
            amountOfLaps = abs(distance)//trackSize
            lapCount += amountOfLaps
            distance += amountOfLaps*trackSize

    print(f"Case #{(testCasesIndex+1)}: {lapCount}")
    distance=0
    lapCount=0
    