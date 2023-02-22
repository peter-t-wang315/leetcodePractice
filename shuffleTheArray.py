# __Big O Time__
# The big O time complexity for this algorithm is O(n) where n is the size of nums. This is because we iterate through half of the nums list. This is a good time complexity as you have to check every element
# of the list and this allows for each item to get hit.

# __Space Complexity__
# The space complexity of this algorithm is O(n) where n is the size of nums. This is because we are creating a copy of nums essentially. This algorithm could be improved on as O(n) is not the best space
# complexity however it is reasonable because otherwise one would have to sacrifice time complexity.

def shuffle(nums, n):
    output = []
    for i in range(len(nums)//2):
        output.append(nums[i])
        output.append(nums[i+n])
    
    return output


if __name__ == "__main__":
    print(shuffle([2,3,5,4,1,7], 3))