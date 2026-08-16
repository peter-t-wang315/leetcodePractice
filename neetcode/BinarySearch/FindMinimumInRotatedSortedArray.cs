public class Solution {
    public int FindMin(int[] nums) {
        int left = 0;
        int right = nums.Length - 1;
        int mid = nums.Length / 2;

        while (left + 1 < right) {
            if (nums[right] < nums[mid]) {
                left = mid;
            }
            else {
                right = mid;
            }
            mid = left + ((right - left) / 2);
        }

        return Math.Min(Math.Min(nums[left], nums[right]), nums[mid]);
    }
}