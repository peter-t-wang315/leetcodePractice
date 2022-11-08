# __Big O time__
# The big O time would be O(n) where n is the size of nums. This is because we are only going through the list once and dictionary lookups are constant time.

# __Space complexity__
# The space complexity for this algorithm is O(n) where n is equal to the k in this function. That is because I am creating a new dictionary of size k+1, but then you
# can just remove the +1 when calculating the big O.

def containsNearbyDuplicate(nums, k):
    currentNumsDict = {}

    for i, val in enumerate(nums):
        if len(currentNumsDict) >= k+1:
            currentNumsDict.pop(nums[i-k-1])
        if currentNumsDict.get(val):
            return True
        currentNumsDict[val] =1
    
    return False


if __name__ == "__main__":
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))