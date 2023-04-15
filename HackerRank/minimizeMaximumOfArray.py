def minimizeArrayValue(nums):
    is_ascending = False
    still_ascending = True
    size = len(nums)
    i = 0
    while is_ascending is False:
        if i==size-1:
            if still_ascending is True:
                break
            else:
                still_ascending = True
                i = 0

        if nums[i] <= nums[i+1]:
            avg = nums[i]+nums[i+1]
            if avg%2==0:
                nums[i] = nums[i+1] = avg//2
            else:
                nums[i] = avg // 2 +1
                nums[i+1] = avg // 2
            if nums[i] != nums[i+1]:
                still_ascending = False
        i+=1
    
    return nums[0]


if __name__ == "__main__":
    print(minimizeArrayValue([3,7,1,6]))