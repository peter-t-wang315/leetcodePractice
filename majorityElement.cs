// __Big O Time__ 
// The big O time of this algorithm is O(n) where n is the size of the nums passed in. This is because the algorithm only iterates through the list one time. This is the optimal time
// as you have to check each item to make sure you find the majority element.

// __Space complexity__
// The space complexity of this algorithm is O(n). This is because you create a dictionary that worst case is the size of nums. This is an ok space complexity but I gotta think about the
// O(1) space complexity solution Leetcode is hinting at.

public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> counts = new Dictionary<int, int>();
        // Majority number, num occurrences.
        (int, int) majorityElement = (0, 0);

        // Count occurrences of each numbers.
        foreach (int num in nums)
        {
            counts[num] = counts.GetValueOrDefault(num, 0) + 1;
            // Nice if statement because now we don't have to iterate over the dictionary again saving us like
            // a little bit of extra time lol.
            if (majorityElement.Item2 < counts[num]){
                majorityElement = (num, counts[num]);
            }
        }

        return majorityElement.Item1;
    }
}