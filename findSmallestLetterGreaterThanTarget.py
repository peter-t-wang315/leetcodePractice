# __Big O Time__
# The big O time of this algorithm is O(n) where n is the input size of the letters array. This is because worst case you iterate over the entire list of letters just to return the first item.
# This time complexity can be improved on by simply using binary search as the letters array is already sorted. This would cut the algorithm time to O(logn) which is much better.

# __Space Complexity__
# The space complexity of this algorithm is O(0). This is because the algorithm doesn't create any new items. This is the best as not using any new space is the best.

def nextGreatestLetter(letters, target):
    for letter in letters:
        if target < letter:
            return letter
    return letters[0]



if __name__ == "__main__":
    print(nextGreatestLetter(["x","x","y","y"], 'z'))