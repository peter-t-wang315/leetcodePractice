# __Big O Time__
# The big O time complexity of this algorithm is O(logn) where n is the length of nums. This is because the algorithm continues to cut the list in half each iteration.
# This is currently the best time complexity as this is just a binary search and for search algorithms there is yet to be discovered a faster time complex algorithm.

# __Space complexity__
# The space complexity of this algorithm is O(1) as there are only 3 created constants. This is the best space complexity as O(1) is the best.

def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    middle = right//2
        

    while left <=right:
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle-1
            middle = right-left
            middle = left + middle
        else:
            left = middle+1
            middle = right - left
            middle = left+ middle

    return left

if __name__ == "__main__":
    print(searchInsert([1,3,5, 9, 10, 11], 5))
    