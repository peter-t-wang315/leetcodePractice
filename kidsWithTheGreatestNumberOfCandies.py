# __Big O Time__
# The big O time of this algorithm is O(n) where n is the input size candies. This is because the algorithm iterates over candies a total of 2 times making it O(2n) which simplifies to O(n).
# This is a reasonable time complexity as to know which kid can have the most candies, you have to check every kid in candies at least once.

# __Space Complexity__
# The space complexity of this algorithm is O(1). This is because the algorithm uses the list given to populate the results. This is a good space complexity as O(1) is the smallest we can get.

def kidsWithCandies(candies, extraCandies):
    most_candies = max(candies)
    for i, kid in enumerate(candies):
        if kid+extraCandies >= most_candies:
            candies[i] = True
        else:
            candies[i] = False

    return candies

if __name__ == "__main__":
    print(kidsWithCandies([2,3,5,1,3], 3))