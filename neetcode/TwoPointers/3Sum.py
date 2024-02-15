# __Big O Time__
# O(n^2) where n is the length of nums. This is slightly more optimized as we skip all positive numbers. So on average run it can be slightly more optimal than
# the counterpart of not skipping non-negative numbers

# __Space Complexity__
# O(n) n being the size of nums. This is because we have to create an output array which can be the size of nums worst case.

def threeSum(nums):
    nums.sort()
    outputs = []
    startingIndex = 0
    currentNum = "start"

    # As we are starting with a sorted array, and we know that our target is 0, no need to go past 0 as anything added to 0 in the positive range is greater than 0
    while startingIndex < len(nums) and nums[startingIndex] <= 0:
        # If our leftmost pointer hasn't seen the number yet. This eliminates the possibility of duplicates
        if nums[startingIndex] != currentNum:
            # Create our current indices
            currentNum = nums[startingIndex]
            leftIndex = startingIndex + 1
            rightIndex = len(nums) - 1
            # Do 2sum
            while leftIndex < rightIndex:
                # If we are above our target
                if currentNum + nums[leftIndex] + nums[rightIndex] > 0:
                    rightIndex -= 1
                # If we are below our target
                elif currentNum + nums[leftIndex] + nums[rightIndex] < 0:
                    leftIndex += 1
                # If we hit our target
                else:
                    outputs.append([currentNum, nums[leftIndex], nums[rightIndex]])
                    # Only need to shift the left pointer like we do in our parent while loop. We must also eliminate the possiblity of dups
                    leftIndex += 1
                    while nums[leftIndex] == nums[leftIndex - 1] and leftIndex < rightIndex:
                        leftIndex += 1
        # Move to the next starting point
        startingIndex += 1

    return outputs

if __name__ == "__main__":
    print(threeSum([0,0,0]))


            
        

