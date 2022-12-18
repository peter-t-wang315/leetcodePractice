# __Big O Time__
# The big O time complexity for this algorithm is O(n) where n is the amount of items in temperatures. This is because at most, each item in the list is used at most twice; once going into a new list, and then
# one more time being popped from said list. This is a reasonable time complexity as you do have to check each item in the list at least once to know how many days it takes before it warms up.

# __Space complexity__
# The space complexity of this algorithm is O(n) where n is the amount of items in temperatures. This is because almost every temperature if not all are stored at one point into the 3 different possible
# lists. This is a reasonable space complexity as the only way to reduce would be to sacrifice time complexity

def dailyTemperatures(temperatures):
    # Create a list that only stores if current temp is lower than previous temp
    listDays = []
    listIndexes = []
    output = temperatures[:]
    sizeListDays = 0
    for i, day in enumerate(temperatures):
        sizeListDays = len(listDays)
        if sizeListDays == 0 or listDays[sizeListDays - 1][0] > day:
            listDays.append((day, i))
        else:
            while len(listDays) > 0 and listDays[len(listDays)-1][0] < day:
                listIndexes.append(listDays[len(listDays)-1][1])
                listDays.pop()
            for indexes in listIndexes:
                output[indexes] = i - indexes
            listIndexes = []
            listDays.append((day, i))

    # Handle extra days
    for day in listDays:
        output[day[1]] = 0

    return output


if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))