# __Big O Time__
# O(n) n being the size of nums. Granted it's not the fastest O(n) it still is. A better solution O(n) solution would be 1) storing indexes in the availableNums 2) run
# through nums again instead of availableNums iterating with an index. Now that we've stored the indexes in availableNums and we have the index, we can simply do 
# target-nums[i] in availableNums and availableNums[target-nums[i]] != i
# This does the checking for us to find the two sum while maintaining indexes without having to do 2 more O(n) calculations.

# __Space Complexity__
# O(n) n being the size of nums

def twoSum(nums, target):
  availableNums={}
  for num in nums:
    if availableNums.get(num):
      availableNums[num] += 1
    else:
      availableNums[num] = 1
  
  for num in availableNums:
    if target-num in availableNums:
      if (target-num == num and availableNums[num] >= 2) or (target-num in availableNums and target-num != num):
        index1 = nums.index(num)
        nums[index1] = "Done"
        index2 = nums.index(target-num)
        return [min(index1, index2), max(index1, index2)]
      
  
  return []
    

if __name__ == "__main__":
  print(twoSum([3,2,5,7,2,2,1], 6))