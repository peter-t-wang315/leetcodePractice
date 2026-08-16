public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int trailingI = 0;
        int currNumCount = 1;
        int k = 1;
        for(int i = 1; i < nums.Length; i++) {
            if (nums[trailingI] == nums[i]){
                if (currNumCount >= 2) {
                    continue;
                }
                currNumCount += 1;
                trailingI += 1;
                nums[trailingI] = nums[i];
                k += 1;
            }
            else {
                k += 1;
                trailingI += 1;
                currNumCount = 1;
                nums[trailingI] = nums[i];
            }
        }

        return k;
    }
}