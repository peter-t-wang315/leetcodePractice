public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0;
        int r = nums.Length - 1;
        int m = nums.Length / 2;
        
        if (nums.Length > 0 && nums[0] == target) {
            return 0;
        }

        while (l <= r)
        {
            m = (l + r) / 2;

            if (nums[m] == target)
            {
                return m;
            }

            // Our left half is sorted
            if (nums[l] <= nums[m])
            {
                if (nums[l] <= target && nums[m] >= target) {
                    r = m;
                }
                else {
                    l = m + 1;
                }
            }
            // Our right half is sorted
            else
            {
                if (nums[r] >= target && nums[m] <= target) {
                    l = m + 1;
                }
                else {
                    r = m;
                }
            }
        }
        return - 1;
    }
}
