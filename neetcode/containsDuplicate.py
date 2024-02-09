# __Big O Time__
# O(n) n being the size of nums

# __Space Complexity__
# The space complexity of this algorithm is O(n) n being the size of nums

def containsDuplicate(nums):
  seen_nums = {}

  for num in nums:
    if seen_nums.get(num):
      return True
    else:
      seen_nums[num] = 1

  return False


if __name__ == "__main__":
  print(containsDuplicate([1,2,3,4,5,6,7,8,1]))