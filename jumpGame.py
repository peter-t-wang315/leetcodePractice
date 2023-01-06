# __Big O Time__ 
# The big O time of this algorithm is O(n) where n is the size of the nums passed in. This is because the algorithm only iterates through the list one time. This is a reasonable time complexity as you would 
# have to check every item in the list at least once to know if jumping is possible.

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because the there are only 2 variables being created no matter the input. This is the best space complexity as constant space is the best.

def canJump(nums):
    curJumpRange = -1
    indexOn = 0
    for i in nums:
        if curJumpRange == 0:
            return False
        if indexOn >= len(nums)-1:
            return True
        if i >= curJumpRange:
            curJumpRange = i
        else:
            curJumpRange -= 1
        indexOn += 1
    
    return False



if __name__ == "__main__":
    print(canJump([1,1,1,0]))