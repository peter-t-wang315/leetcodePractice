public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> seenNums = new(nums);
        int longestConsecutive = 0;
        int currCount = 0;

        foreach (int num in seenNums)
        {
            if (seenNums.Contains(num - 1)){
                continue;
            }
            while (seenNums.Contains(num+currCount)) currCount++;
            if (currCount > longestConsecutive) longestConsecutive = currCount;

            currCount = 0;
        }

        return longestConsecutive;
    }
}
