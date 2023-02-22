# __Big O Time__
# The big O time complexity of this algorithm is O(1). This is because there are always at most 4 operations and the amount of operations doesn't depend on any input. This
# is the best time complexity as constant time is the best.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because there is only ever one constant that is created. This is the best space complexity as constant space
# is the best.

def countOdds(low, high):
    count = (high-low) // 2
    if low % 2 == 1 or high %2 == 1:
        count += 1

    return count

if __name__ == "__main__":
    print(countOdds(4, 7))