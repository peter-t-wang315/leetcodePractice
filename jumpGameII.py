# __Big O Time__
# The big O time complexity of this algorithm is O(n) where n is the size of the inputted list. This is because no matter what, we will index at least once down the array
# and never traverse back. This is an acceptable time complexity as we have to check every item in the list at least once.

# __Space Complexity__
# The space complexity of this algorithm is O(1). This is because we are only creating a set amount of integers meaning they cannot scale in memory with the length of any input. This is the best space complexity
# as constant memory is the most optimal.

def jump(nums):
    if len(nums) < 2:
        return 0
    jumps = 1 
    longest_relative_jump = 0
    current_jump = nums[0]
    i = 0
    while i+current_jump+1 < len(nums):
        for helper_i in range(1,current_jump+1):
            if longest_relative_jump < nums[i+helper_i]+helper_i:
                longest_relative_jump = nums[i+helper_i]+helper_i
                next_jump = nums[i+helper_i]
                jump_index = i+helper_i
        i = jump_index
        current_jump = next_jump
        longest_relative_jump = 0
        jumps+=1

    return jumps

    

            


if __name__ == "__main__":
    print(jump([2,3,1,1,4]))
