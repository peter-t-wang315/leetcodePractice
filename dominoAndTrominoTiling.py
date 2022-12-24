# __Big O time__
# The time complexity of this algorithm is O(n) where n is the size of the input list. This is because the algorithm iterates the entire range of n. This is a reasonable time complexity as we need to iterate through each
# number at least once to find the amount of possibilities.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because there are only always 4 variables created regardless of the input. This is the best space complexity as constant space is the best.

def numTilings(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    prev1 = 2
    prev2 = 1
    prev3 = 1
    for _ in range(2,n):
        current = prev1 * 2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = current
    return current % (10**9+7)


if __name__ == "__main__":
    print(numTilings(30))