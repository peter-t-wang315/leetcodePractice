public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int left = 0;
        int right = piles.Max();
        int mid = piles.Max() / 2;

        while (left < right) {
            mid = left + (right - left) / 2;
            if (KoKoCanFinish(mid)) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }
        bool KoKoCanFinish(int BPH) {
            int hourCount = 0;
            foreach (int bananaCount in piles) {
                hourCount += (int)Math.Ceiling((double)bananaCount / BPH);
                if (hourCount > h) {
                    return false;
                }
            }
            return hourCount <= h;
        }
        return right;
    }
}