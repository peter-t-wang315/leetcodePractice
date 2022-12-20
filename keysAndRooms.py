# __Big O time__
# The big O time complexity is O(n^2) where n is the length of the list rooms. This is because at a worse case, we check each room once, but each room has n-1 amount of keys with all the same keys as the other
# rooms but is missing the final key. The reason why it checks each room's keys is because my algorithm turns each room's keys into a set.

# __Space complexity__
# The space complexity of this algorithm is O(n). This is because there are only 3 sets that can hold the max amount of rooms which would technically make O(3n). But then you remove constants and the space
# lowers back to O(n).

def canVisitAllRooms(rooms):
    totalKeys = set([0]) | set(rooms[0])
    newKeys = set(rooms[0])
    tempNewKeys = set()
    # Iterate enough times that we can go through each room if possible
    while newKeys:
        for newKey in newKeys:
            tempNewKeys = tempNewKeys | set(rooms[newKey])
        # Reset newKeys!!
        newKeys = tempNewKeys - totalKeys
        tempNewKeys = set()
        totalKeys = totalKeys | newKeys

    if len(totalKeys) == len(rooms):
        return True
    return False


if __name__ == "__main__":
    print(canVisitAllRooms([[1, 0, 5],[1, 3, 2],[3],[4], [4], []]))