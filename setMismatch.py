def findErrorNums(nums):
    numsDict = {}
    for i in range(len(nums)):
        if numsDict.get(nums[i]):
            dupNum = nums[i]
        numsDict[nums[i]] = 1
    
    for i in range(1, len(nums)+1):
        if not numsDict.get(i):
            return [dupNum, i]


if __name__ == "__main__":
    print(findErrorNums([1,2,2,3]))